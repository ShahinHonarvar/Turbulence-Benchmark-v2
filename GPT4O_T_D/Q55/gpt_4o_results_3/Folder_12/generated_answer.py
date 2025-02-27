def lists_with_product_equal_n(circular_list):

    def find_sublist_with_product(start, length, target):
        product = 1
        sublist = []
        for i in range(length):
            index = (start + i) % len(circular_list)
            product *= circular_list[index]
            sublist.append(circular_list[index])
            if product == target:
                return sublist
            if product == 0:
                break
        return None
    result = []
    n = len(circular_list)
    for length in range(1, n + 1):
        for start in range(n):
            sublist = find_sublist_with_product(start, length, -18)
            if sublist is not None:
                result.append(sublist)
    return result