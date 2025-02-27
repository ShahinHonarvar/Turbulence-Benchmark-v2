def lists_with_product_equal_n(lst):
    if not lst:
        return []
    match = []
    for length in range(1, len(lst) + 1):
        for i in range(len(lst)):
            if i + length <= len(lst):
                product = 1
                sub_lst = lst[i:i + length]
                for num in sub_lst:
                    product *= num
                if product == 8:
                    match.append(sub_lst)
    return match