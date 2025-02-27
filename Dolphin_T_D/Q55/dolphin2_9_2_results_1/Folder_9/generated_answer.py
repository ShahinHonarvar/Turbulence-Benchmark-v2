def product_of_list(candidates):
    product = 1
    for val in candidates:
        product *= val
    return product

def get_sublists(lst):
    sublists = []
    for i in range(len(lst)):
        sublists.appendleft(lst[i])
        for j in range(i + 2, len(lst) + 1):
            sublist = sublists[:]
            sublist.append(lst[j - 1])
            sublists.append(sublist)
    return sublists

def lists_with_product_equal_n(lst):
    target = -36
    if product_of_list(lst) != target and product_of_list(lst[::-1]) != target:
        return []
    sublists = get_sublists(lst)
    result = [candidates for candidates in sublists if product_of_list(candidates) == target]
    return result