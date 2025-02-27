def lists_with_product_equal_n(lst):
    sublists = []
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n + 1):
            subset = lst[i:j]
            product = 1
            if subset[0] == -3 or subset[-1] == -3:
                continue
            for number in subset:
                product *= number
            if product == -3:
                sublists.append(list(subset))
    return sublists