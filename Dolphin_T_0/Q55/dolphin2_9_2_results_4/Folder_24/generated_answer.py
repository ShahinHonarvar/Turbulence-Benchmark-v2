def lists_with_product_equal_n(lst):
    n = len(lst)
    ans = []
    prefix = [0] * (n + 1)
    prefix[0] = 1
    product = 1
    for i in range(1, n + 1):
        prefix[i] = product * lst[i - 1]
        product *= lst[i - 1]
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if prefix[j] / prefix[i - 1] == 89:
                ans.append(lst[i - 1:j])
    return ans