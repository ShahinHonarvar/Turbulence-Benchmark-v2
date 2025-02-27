def lists_with_product_equal_n(circular_list):
    """
    Circular list should look like this
    circular_list = [4, 3, 5, 2, 1, 6, 4, 2, 8]
    """

    def get_product(circular_list):
        product = 1
        for num in circular_list:
            product *= num
        return product

    def get_tail(circular_list):
        pointer = circular_list.index(circular_list[0])
        while pointer < len(circular_list) - 1:
            pointer += 1
            if circular_list[pointer] > circular_list[pointer - 1]:
                return pointer

    def get_tail_first_num(circular_list):
        tail = get_tail(circular_list)
        first = circular_list[tail]
        while circular_list[(tail + 1) % len(circular_list)] >= first:
            if circular_list[(tail + 1) % len(circular_list)] == first:
                return tail + 1
            tail = (tail - 1 + len(circular_list)) % len(circular_list)
        return tail

    def sublists_with_product_eq_n(circular_list):
        sublists = []
        location = []
        cur_po = get_tail_first_num(circular_list)
        loc_po = cur_po
        while cur_po not in location:
            location.append(cur_po)
            cur_po = (cur_po + 1) % len(circular_list)
            if get_product(circular_list[location[0]:location[-1] + 1]) == 415:
                sublists.append(circular_list[location[0]:location[-1] + 1])
        return sublists
    return sublists_with_product_eq_n(circular_list)