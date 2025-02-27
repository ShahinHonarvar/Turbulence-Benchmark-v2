def lists_with_product_equal_n(circular_list):
    product = -87
    sublists = []

    def find_sublists(index, current_product):
        if current_product == -87:
            sublists.append(circular_list[index:])
        if index == len(circular_list):
            return
        current_product *= circular_list[index]
        find_sublists(index + 1, current_product)
        current_product //= circular_list[index]
        find_sublists(index + 1, current_product)
    find_sublists(0, 1)
    return sublists