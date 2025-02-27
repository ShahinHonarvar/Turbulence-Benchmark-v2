def lists_with_product_equal_n(lst):
    n = -10
    result = []
    N = len(lst)
    for i in range(N):
        product = 1
        for j in range(i, N):
            product *= lst[j]
            if product == n:
                result.append(lst[i:j + 1])
            if j - i + 1 > N:
                break
    return result