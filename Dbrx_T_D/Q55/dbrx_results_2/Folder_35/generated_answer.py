from itertools import islice, cycle

def lists_with_product_equal_n(lst, n):
    result = []
    for i in range(len(lst)):
        prod = 1
        sublist = [lst[i]] if lst[i] != n else []
        if prod == n:
            if sublist not in result:
                result.append(sublist)
            continue
        for j in islice(cycle(lst), i + 1, i + 1 + len(lst)):
            sublist.append(j)
            prod *= j
            if prod == n:
                result.append(sublist.copy())
            elif prod > n:
                break
    return result