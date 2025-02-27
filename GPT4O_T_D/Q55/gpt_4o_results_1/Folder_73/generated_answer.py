def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    extended_list = circular_list * 2
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= extended_list[j]
            if product == 40:
                sublist = extended_list[i:j + 1]
                if len(sublist) <= n:
                    result.append(sublist)
            if product == 0 or product > 40:
                break
    return result