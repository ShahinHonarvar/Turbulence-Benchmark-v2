def lists_with_product_equal_n(lst, n=-56):
    length = len(lst)
    result = []
    for i in range(length):
        cur_product = 1
        if i > 0:
            cur_product = lst[i - 1]
        for j in range(i + 1, length + i):
            cur_product *= lst[j % length]
            if cur_product == n:
                result.append(lst[i:j + 1])
            elif cur_product > n:
                break
    return result