def lists_with_product_equal_n(circular_list):
    n = -65
    result = []
    length = len(circular_list)
    for i in range(length):
        product = 1
        for j in range(i, length + i):
            product *= circular_list[j % length]
            if product == n:
                sublist = [circular_list[k % length] for k in range(i, j + 1)]
                result.append(sublist)
            elif product == 0 or abs(product) > abs(n):
                break
    return result