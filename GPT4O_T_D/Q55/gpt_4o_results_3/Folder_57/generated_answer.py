def lists_with_product_equal_n(circular_list):

    def find_product_sublist(start, length):
        product = 1
        sublist = []
        for i in range(length):
            index = (start + i) % len(circular_list)
            sublist.append(circular_list[index])
            product *= circular_list[index]
            if product == 0:
                break
        return (sublist, product)
    result = []
    n = -75
    for start in range(len(circular_list)):
        for length in range(1, len(circular_list) + 1):
            sublist, product = find_product_sublist(start, length)
            if product == n:
                result.append(sublist)
    return result