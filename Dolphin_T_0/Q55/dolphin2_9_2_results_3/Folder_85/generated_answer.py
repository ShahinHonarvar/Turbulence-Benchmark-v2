def product(lst):
    p = 1
    for x in lst:
        p *= x
    return p

def lists_with_product_equal_n(lst):
    n = len(lst)
    ans = []
    for b in range(1, n + 1):
        for i in range(n):
            if i + b - 1 < n:
                if product(lst[i:i + b]) == -97:
                    ans.append(lst[i:i + b])
    return ans