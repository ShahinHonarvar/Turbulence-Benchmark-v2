def lists_with_product_equal_n(circular_list):
    n = -91
    result = []
    for i in range(len(circular_list)):
        product = 1
        for j in range(i, len(circular_list)):
            product *= circular_list[j]
            if product == n:
                result.append(circular_list[i:j + 1])
            if product > n:
                break
        if i > 0 and product != n:
            product = 1
            for j in range(i, len(circular_list) + i):
                product *= circular_list[j % len(circular_list)]
                if product == n:
                    sublist = [circular_list[k % len(circular_list)] for k in range(i, j + 1)]
                    result.append(sublist)
                if product > n:
                    break
    return result