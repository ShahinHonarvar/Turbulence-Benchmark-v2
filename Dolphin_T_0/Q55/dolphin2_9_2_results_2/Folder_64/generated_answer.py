def lists_with_product_equal_n(lst):
    if not lst:
        return []
    lst_len = len(lst)
    lst = lst + lst[:-1]
    ans = []
    for i in range(lst_len):
        product = 1
        for j in range(i, i + lst_len):
            product *= lst[j % lst_len]
            if product % 3 == 0 and lst[j % lst_len] % 3 == 0:
                ans.append(lst[i:j % lst_len + lst_len])
    ans = list(dict.fromkeys(map(tuple, ans)))
    ans = [list(tup) for tup in ans]
    return ans