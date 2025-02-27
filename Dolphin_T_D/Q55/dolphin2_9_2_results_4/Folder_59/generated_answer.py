def lists_with_product_equal_n(lst, n=-3):
    l = len(lst)
    result = []
    for i in range(l):
        tmp = [lst[i]]
        for j in range(i + 1, l + i):
            tmp.append(lst[j % l])
            if j - i + 1 > l:
                break
            product = 1
            for k in tmp:
                product *= k
            if product == n:
                result.append(tmp)
    return result