def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    for i in range(n):
        product = 1
        sublist = []
        for j in range(n):
            idx = (i + j) % n
            product *= circular_list[idx]
            sublist.append(circular_list[idx])
            if product == -115:
                result.append(sublist.copy())
            if j == n - 1:
                break
            if product == 0:
                break
            if product > 115 and product < -115 and (circular_list[idx] != 0):
                break
    return result