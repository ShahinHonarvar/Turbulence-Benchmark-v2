def lists_with_product_equal_n(lst):
    sublists = []
    n = len(lst)
    for i in range(n):
        product = lst[i]
        if product == 990 and n == 1:
            sublists.append([lst[i]])
        elif product == 990 and n != 1 and (lst[i - 1] == 1):
            sublists.append([lst[i]])
        elif product < 990:
            continue
        else:
            sublist = [lst[i]]
            j = i + 1
            while j != i:
                if j == n:
                    j = 0
                product = product * lst[j]
                if product == 990:
                    sublists.append(sublist)
                    j = i + 1
                elif product > 990:
                    break
                else:
                    sublist.append(lst[j])
                    j += 1
    return sublists