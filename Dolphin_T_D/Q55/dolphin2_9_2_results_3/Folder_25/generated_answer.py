def lists_with_product_equal_n(lst):
    multi = lambda a, b: a * b
    if len(lst) == 1:
        return [] if lst[0] != -32 else [lst]
    elif len(lst) == 2:
        return [] if multi(lst[0], lst[1]) != -32 else [lst]
    elif len(lst) > 2:
        result = []
        for i in range(len(lst)):
            product = 1
            for j in range(i, len(lst)):
                product = multi(product, lst[j % len(lst)])
                if product == -32:
                    result.append(lst[i:j + 1])
        return result
    else:
        return []