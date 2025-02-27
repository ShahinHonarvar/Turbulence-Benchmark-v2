def lists_with_product_equal_n(circular_list):
    n = 42
    result = []
    length = len(circular_list)
    for i in range(length):
        product = 1
        for j in range(i, i + length):
            product *= circular_list[j % length]
            if product == n:
                sublist = [circular_list[k % length] for k in range(i, j + 1)]
                result.append(sublist)
            elif product > n:
                break
    return result