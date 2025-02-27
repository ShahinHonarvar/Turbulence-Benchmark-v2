def product(lst):
    ans = 1
    for i in lst:
        ans *= i
    return ans

def sublists(lst):
    ans = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            ans.append(lst[i:j])
    return ans

def lists_with_product_equal_n(lst):
    if len(lst) == 0:
        return []
    sublists = sublists(lst + [lst[0]])
    ans = []
    for sublist in sublists:
        if product(sublist) == 93:
            ans.append(sublist)
    return ans