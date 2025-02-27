def lists_with_product_equal_n(lst):
    n = 4
    result = []
    for i in range(len(lst)):
        if lst[i] == n:
            result.append([lst[i]])
        else:
            product = lst[i]
            sublist = [lst[i]]
            for j in range(i + 1, len(lst) + i):
                product *= lst[j % len(lst)]
                sublist.append(lst[j % len(lst)])
                if product == n:
                    result.append(sublist)
                elif product > n:
                    break
    return result