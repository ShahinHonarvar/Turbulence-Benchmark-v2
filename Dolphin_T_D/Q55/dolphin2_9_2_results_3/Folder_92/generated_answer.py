def lists_with_product_equal_n(lst):
    result = []
    all_subsets = [combinations(lst, i) for i in range(len(lst) + 1)]
    flat_list = [item for sublist in all_subsets for item in sublist]
    for subset in flat_list:
        product = 1
        for element in subset:
            product *= element
        if product == 5:
            result.append(list(subset))
    return result