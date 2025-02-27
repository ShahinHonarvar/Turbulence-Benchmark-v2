def lists_with_product_equal_n(lst):
    if len(lst) == 0:
        return []
    else:
        result = []
        for i in range(len(lst)):
            product = 1
            for j in range(i, len(lst)):
                product *= lst[j]
                if product > 74:
                    break
                elif product == 74 and [lst[k] for k in range(i, j + 1)] not in result:
                    result.append([lst[k] for k in range(i, j + 1)])
        return result