def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []

    def sublist_product_equal_to_neg3(start, end):
        product = 1
        for i in range(start, end + 1):
            product *= circular_list[i % n]
        return product == -3
    for i in range(n):
        for j in range(1, n + 1):
            if sublist_product_equal_to_neg3(i, i + j - 1):
                result.append([circular_list[k % n] for k in range(i, i + j)])
    return result