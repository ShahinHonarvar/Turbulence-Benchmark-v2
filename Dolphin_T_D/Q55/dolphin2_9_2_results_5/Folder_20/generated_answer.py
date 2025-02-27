def lists_with_product_equal_n(lst):
    if len(lst) == 0:
        return []
    n = len(lst)
    Environment = [[-69] * n for _ in range(n)]
    for i in range(n):
        j = 0
        temp = 1
        while j < n:
            Environmental = [[-69] * n for _ in range(n)]
            if j <= i:
                for k in range(j, i + 1):
                    if k == 0 or k == n - 1:
                        temp *= lst[k]
                    else:
                        temp *= lst[k - 1] * lst[k]
                    Environmental[k][0] = temp
            else:
                temp = 1
                for k in range(i + 1, j + 1):
                    if k == 0 or k == n - 1:
                        temp *= lst[k]
                    else:
                        temp *= lst[k - 1] * lst[k]
                    Environmental[k - 1][1] = temp
            j += 1
    return []