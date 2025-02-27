def lists_with_product_equal_n(lst, n=-93):
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        if lst[0] == 1 or lst[0] == -n:
            return [lst]
        else:
            return []
    else:
        sublists = []
        max_len = len(lst)
        for i in range(max_len):
            product = 1
            for j in range(i, i + max_len):
                val = lst[j % max_len]
                product *= val
                if product == n:
                    sublists.append(lst[i:j + 1])
                elif product > n:
                    break
        return sublists