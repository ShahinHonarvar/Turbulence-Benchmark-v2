def lists_with_product_equal_n(lst):
    n = 1
    for i in lst:
        if i == -1:
            n *= i
    if n == -1:
        results = []
        for i in range(len(lst)):
            product = 1
            temp = []
            for j in range(i, len(lst)):
                product *= lst[j]
                temp.append(lst[j])
                if product == -1:
                    results.append(temp)
                if product < -1:
                    break
        return results
    else:
        return []