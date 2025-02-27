def lists_with_product_equal_n(circular_list):
    n = 54
    result = []
    for i in range(len(circular_list)):
        sublist = circular_list[i:] + circular_list[:i]
        for j in range(len(sublist)):
            if len(sublist) - j >= sublists_with_product_equal_n_ITERATIVE(sublist[j:], n):
                break
        product = 1
        for k in sublist[j:j + sublists_with_product_equal_n_ITERATIVE(sublist[j:], n)]:
            product *= k
        if product == n:
            result.append(sublist[j:j + sublists_with_product_equal_n_ITERATIVE(sublist[j:], n)])
    return result

def sublists_with_product_equal_n_ITERATIVE(lst, n):
    if n == 1:
        return 1
    elif not lst:
        return 0
    elif lst[0] == 0:
        return sublists_with_product_equal_n_ITERATIVE(lst[1:], n)
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(len(lst)):
        j = 1
        while j * lst[i] <= n:
            dp[j * lst[i]] += dp[j]
            j += 1
    return dp[n]