def lists_with_product_equal_n(circular_list):

    def get_product_sublist(start, end):
        product = 1
        sublist = []
        length = len(circular_list)
        for i in range(end - start + 1):
            index = (start + i) % length
            sublist.append(circular_list[index])
            product *= circular_list[index]
        return (product, sublist)
    result = []
    length = len(circular_list)
    for start in range(length):
        for end in range(start, start + length):
            product, sublist = get_product_sublist(start, end)
            if product == 47:
                result.append(sublist)
    return result