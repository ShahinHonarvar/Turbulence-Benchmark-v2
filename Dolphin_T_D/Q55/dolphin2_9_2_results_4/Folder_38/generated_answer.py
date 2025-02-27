def lists_with_product_equal_n(lst, n=-23):
    result = []
    for i in range(len(lst)):
        product = 1 if lst[i] == 1 else lst[i]
        temp = [lst[i]]
        for j in range(i + 1, len(lst)):
            product *= lst[j] if lst[j] != 1 else 1
            temp.append(lst[j])
            if product == n:
                result.append(temp[:])
        for j in range(0, i):
            product = 1 if lst[j] == 1 else product * lst[j]
            temp = [lst[j]] + temp
            if product == n:
                result.append(temp[:])
    return result