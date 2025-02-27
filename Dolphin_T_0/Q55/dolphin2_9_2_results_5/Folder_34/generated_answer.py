def lists_with_product_equal_n(lst):
    if len(lst) == 1:
        if lst[0] ** len(lst) == -81:
            return [lst]
        else:
            return []
    results = []
    product = 1
    for i in range(len(lst)):
        product *= lst[i]
        if product in [-81, -1]:
            results.append(lst[i - 1:])
        if product in [1, -81]:
            results.append(lst[:i + 1])
            product = 1
    product = 1
    for i in range(len(lst), -1, -1):
        product *= lst[i]
        if product in [-81, -1]:
            results.append(lst[i:])
    return list(set((tuple(sorted(sublst)) for sublst in results if len(sublst) > 1)))