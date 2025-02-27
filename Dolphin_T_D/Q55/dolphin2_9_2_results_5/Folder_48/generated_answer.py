def lists_with_product_equal_n(lst):
    if not lst:
        return []
    result = []
    n_len = len(lst)
    prod = 1
    for i in range(n_len):
        prod *= lst[i]
    if prod != 990:
        return result
    prod_set = set()
    prod_dict = dict()
    cum_prod = 1
    for i in range(n_len):
        cum_prod *= lst[i]
        if cum_prod in prod_set:
            result.append(prod_dict[cum_prod][1])
        else:
            prod_set.add(cum_prod)
            prod_dict[cum_prod] = (prod_dict.get(cum_prod * 990 // (prod // lst[i]), []), i + 1)
    return result