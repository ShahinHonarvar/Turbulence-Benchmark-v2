def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        product = lst[i]
        sublist = [lst[i]]
        for j in range((i + 1) % len(lst), (i + len(lst)) % len(lst)):
            sublist.append(lst[j])
            product *= lst[j]
            if product == -36:
                result.append(sublist[:])
    return result