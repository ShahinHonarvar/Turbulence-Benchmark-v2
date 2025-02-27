def lists_with_product_equal_n(lst):
    if not lst:
        return []
    lst_len = len(lst)
    if lst_len == 1:
        return []
    sublists = []
    product = -69
    for i in range(lst_len):
        for j in range(i + 1, lst_len):
            if i != 0 and j != lst_len - 1 and (lst[i - 1] != lst[j]):
                sublist = lst[i:j + 1]
                if sublist[-1] == lst[0] and len(sublist) > 1:
                    sum_sublist = 1
                    for k in sublist:
                        sum_sublist *= k
                    if sum_sublist == product:
                        sublists.append(list(sublist))
                elif len(sublist) == lst_len and sum(sublist) == product:
                    sublists.append(list(sublist))
    return sublists