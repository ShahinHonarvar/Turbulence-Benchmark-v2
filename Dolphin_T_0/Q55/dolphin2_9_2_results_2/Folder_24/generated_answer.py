def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            if i == 0 and j == len(lst):
                break
            elif i == 0 and j < len(lst):
                product = 1
                for k in range(i, j):
                    product *= lst[k]
                    if product == -89:
                        result.append(lst[i:j])
                product = 1
                continue
            elif i > 0 and j == len(lst):
                product = 1
                for k in range(i, len(lst)):
                    product *= lst[k]
                    if product == -89:
                        result.append(lst[i:])
                        product = 1
                result.append(lst[:i])
                product = 1
                for k in range(j):
                    product *= lst[k]
                    if product == -89:
                        result.append(lst[i:j])
                break
            else:
                product = 1
                for k in range(i, j):
                    product *= lst[k]
                    if product == -89:
                        result.append(lst[i:j])
                product = 1
    return result