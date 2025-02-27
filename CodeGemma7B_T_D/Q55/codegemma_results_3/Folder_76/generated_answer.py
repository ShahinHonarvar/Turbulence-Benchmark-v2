def lists_with_product_equal_n(lst):
    ans = []
    total = 1
    for i in range(len(lst)):
        total *= lst[i]
        if total == 247:
            ans.append(lst[i:])
            total = 1
        elif total > 247:
            total = lst[i]
            ans.append(lst[i:])
            total = 1
    if not ans:
        return []
    return ans