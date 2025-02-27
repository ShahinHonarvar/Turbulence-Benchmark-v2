def lists_with_product_equal_n(lst):
    prod_n = 1
    for num in lst:
        prod_n *= num
    if prod_n == 0:
        sublists = []
        length = len(lst)
        for start_idx in range(length):
            for end_idx in range(start_idx + 1, length + start_idx):
                sublist = lst[start_idx:end_idx % length]
                product = 1
                for num in sublist:
                    product *= num
                if product == 0:
                    sublists.append(sublist)
        return sublists
    else:
        return []