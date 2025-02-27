def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    product_map = {1: [[]]}
    cur_product = 1
    for i in range(n):
        cur_product *= lst[i]
        if cur_product in product_map:
            product_map[cur_product].append(lst[i])
        else:
            product_map[cur_product] = [lst[i]]
    cur_idx = n
    while cur_idx < 2 * n - 1:
        cur_product /= lst[cur_idx - n]
        if cur_product in product_map:
            for num in product_map[cur_product]:
                if num != lst[cur_idx - n]:
                    result.append(product_map[cur_product] + [num])
        cur_idx += 1
    result = list(filter(lambda x: x[0] != x[-1] and x[0] != x[-2] and (x[-1] != x[0]) and (x[-1] != x[1]) and (x[0] * x[-1] == -23), result))
    return result