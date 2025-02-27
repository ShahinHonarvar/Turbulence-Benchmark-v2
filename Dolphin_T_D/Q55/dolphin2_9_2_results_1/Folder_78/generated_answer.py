def lists_with_product_equal_n(circular_list):
    sublists = []
    n = len(circular_list)
    for i in range(n):
        for j in range(i + 1, n + 1):
            if i == 0 and j == n:
                product = 1
                for k in range(i, n):
                    product *= circular_list[k]
                for k in range(0, j):
                    product *= circular_list[k]
            elif i == j:
                product = circular_list[i]
            elif i > j:
                product = circular_list[i]
                for k in range(i + 1, n):
                    product *= circular_list[k]
                for k in range(0, j):
                    product *= circular_list[k]
            else:
                product = circular_list[i]
                for k in range(i + 1, j):
                    product *= circular_list[k]
            if product == 74:
                sublist = circular_list[i:j]
                sublists.append(sublist)
    return sublists