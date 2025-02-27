def lists_with_product_equal_n(circular_list):
    target_product = -17
    n = len(circular_list)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            index = (i + j) % n
            product *= circular_list[index]
            if product == target_product:
                sublist = []
                for k in range(j + 1):
                    sublist.append(circular_list[(i + k) % n])
                result.append(sublist)
            if j == n - 1:
                break
    return result