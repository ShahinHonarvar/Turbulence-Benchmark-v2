def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    if n == 0:
        return []
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            index = (i + j) % n
            product *= circular_list[index]
            if product == -779:
                sublist = []
                for k in range(j + 1):
                    sublist.append(circular_list[(i + k) % n])
                result.append(sublist)
            if abs(product) > abs(-779) and product != 0:
                break
    return result