def lists_with_product_equal_n(circular_list):

    def product_equal_n(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product == 32
    length = len(circular_list)
    all_sublists = []
    for size in range(1, length + 1):
        for start in range(length):
            end = start + size
            sublist = circular_list[start:end]
            if product_equal_n(sublist):
                all_sublists.append(sublist)
    return all_sublists