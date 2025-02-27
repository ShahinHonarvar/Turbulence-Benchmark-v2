def lists_with_product_equal_n(lst):
    """
    circular list product equal -3
    """
    products = [lst[i] * lst[(i + 1) % len(lst)] for i in range(len(lst))]
    result = []
    for i in range(len(products)):
        if products[i] == -3:
            result.append([lst[i], lst[(i + 1) % len(lst)]])
            if lst[i] == lst[(i + 1) % len(lst)]:
                result.append([lst[i], lst[(i + 1) % len(lst)], lst[(i + 2) % len(lst)]])
    return result