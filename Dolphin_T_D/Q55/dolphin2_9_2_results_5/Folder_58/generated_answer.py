def lists_with_product_equal_n(lst):
    n = len(lst)
    if n == 0:
        return []
    elif n == 1:
        if lst[0] == 733:
            return [lst]
        else:
            return []
    else:
        sublists = []
        for i in range(n):
            product = 1
            for j in range(i, n):
                product *= lst[j % n]
                if product == 733:
                    sublists.append(lst[i:j + 1])
        return sublists