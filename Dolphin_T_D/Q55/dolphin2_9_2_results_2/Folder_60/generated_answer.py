def lists_with_product_equal_n(lst):
    if not lst:
        return []
    head = lst[0]
    rest = lst[1:]
    result = lists_with_product_equal_n_helper(rest + [head], [head])
    if not result:
        return []
    else:
        return result

def lists_with_product_equal_n_helper(lst, product_set):
    if not lst:
        return []
    current_product = 1
    sublists = []
    for index in range(len(lst)):
        current_product *= lst[index]
        sublists.append(lst[:index + 1])
        if current_product in product_set:
            return sublists
        else:
            product_set.add(current_product)
    return lists_with_product_equal_n_helper(lst[1:], product_set)