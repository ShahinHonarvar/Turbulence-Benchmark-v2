def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        for j in range(i, i + n):
            sublist = circular_list[i:(j + 1) % n] + circular_list[:(j + 1) % n] if j >= n else circular_list[i:(j + 1) % n]
            if len(sublist) > 0:
                product = 1
                for x in sublist:
                    product *= x
                if product == -81:
                    result.append(sublist)
    return result