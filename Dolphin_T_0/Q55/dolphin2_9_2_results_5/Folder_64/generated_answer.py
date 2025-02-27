def lists_with_product_equal_n(lst):
    result = []
    n = 1
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            sublist = lst[i:j]
            if n == 3:
                result.append(sublist)
            product = 1
            for k in sublist:
                if k == 0:
                    product = 0
                    break
                product *= k
            if product == 3:
                n = 1
            else:
                n += 1
    return result