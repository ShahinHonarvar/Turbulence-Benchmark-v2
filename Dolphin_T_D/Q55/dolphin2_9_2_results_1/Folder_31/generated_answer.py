def lists_with_product_equal_n(lst):
    if not lst:
        return []
    sublists = []
    n = len(lst)
    for i in range(n):
        prod = lst[i]
        if prod == -16:
            sublists.append([lst[i]])
        elif prod == 1:
            continue
        else:
            j = i + 1
            while j != i:
                j %= n
                prod *= lst[j]
                if prod == -16:
                    sublists.append(lst[i:j + 1])
                elif prod > -16:
                    break
                j += 1
    return sublists