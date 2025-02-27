def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= lst[j]
            if product == 96:
                result.append(lst[i:j + 1])
            elif product > 96:
                break
        if i != 0:
            for j in range(i):
                product *= lst[j]
                if product == 96:
                    result.append(lst[i:] + lst[:j + 1])
                elif product > 96:
                    break
    return result