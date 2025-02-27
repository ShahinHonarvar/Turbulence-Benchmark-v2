def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        for j in range(i, i + n):
            sublist = circular_list[i:(j + 1) % n]
            if len(sublist) > 1 or (len(sublist) == 1 and i == j):
                product = 1
                for x in sublist:
                    product *= x
                if product == -97:
                    result.append(sublist)
    return result