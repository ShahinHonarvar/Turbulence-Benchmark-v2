def lists_with_product_equal_n(circular_list):

    def circular_index(idx, length):
        return idx % length

    def product_of_sublist(sublist):
        prod = 1
        for num in sublist:
            prod *= num
        return prod
    length = len(circular_list)
    result = []
    for start in range(length):
        for size in range(1, length + 1):
            sublist = [circular_list[circular_index(start + i, length)] for i in range(size)]
            if product_of_sublist(sublist) == 54:
                result.append(sublist)
    return result