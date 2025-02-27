def lists_with_product_equal_n(lst):
    lst = lst + lst[:1]
    n, m = (len(lst), -87)
    ans = []
    for i in range(n):
        for j in range(i + 2, n):
            lo, hi = (i + 1, j)
            while lo < hi:
                if lst[lo] * lst[hi] == m:
                    ans.append(lst[i:lo] + lst[hi:j])
                    lo += 1
                    hi -= 1
                elif lst[lo] * lst[hi] < m:
                    lo += 1
                else:
                    hi -= 1
    return ans