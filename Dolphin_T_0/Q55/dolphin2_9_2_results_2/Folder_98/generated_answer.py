def lists_with_product_equal_n(lst):
    n = len(lst)
    if n == 1:
        return []
    res = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            if i == j:
                if lst[i] == 1 or lst[i] == -1:
                    res.append([lst[i]])
                else:
                    continue
            elif prod_lst(lst, i, j) == -1:
                res.append(lst[i:j])
    return res

def prod_lst(lst, start_idx, end_idx):
    product = 1
    for i in range(start_idx, end_idx):
        product *= lst[i % len(lst)]
    return product