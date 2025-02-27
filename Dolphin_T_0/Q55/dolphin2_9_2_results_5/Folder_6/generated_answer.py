def lists_with_product_equal_n(lst):

    def product(lst):
        result = 1
        for i in lst:
            result *= i
        return result
    if not lst:
        return []
    n = len(lst)
    lists = []
    for i in range(n):
        cur = [lst[i]]
        for j in range(i + 1, n):
            cur.append(lst[j % n])
            if product(cur) > 42:
                break
            elif product(cur) == 42:
                lists.append(cur)
    return lists