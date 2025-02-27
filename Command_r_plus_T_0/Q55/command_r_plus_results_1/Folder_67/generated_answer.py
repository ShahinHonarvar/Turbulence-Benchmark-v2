def lists_with_product_equal_n(circular_list):

    def product_equal_n(start, end):
        product = 1
        for i in range(start, end + 1):
            product *= circular_list[i % len(circular_list)]
        return product == 33
    sublists = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list)):
            if product_equal_n(i, j):
                sublists.append(circular_list[i:j + 1])
    return sublists