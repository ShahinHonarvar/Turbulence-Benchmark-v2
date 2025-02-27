def lists_with_product_equal_n(circular_list):
    products = {}
    current_product = 1
    current_sublist = []
    for x in circular_list + circular_list:
        current_product *= x
        current_sublist.append(x)
        if current_product == -33:
            products[tuple(current_sublist)] = True
            current_product = 1
            current_sublist = []
        elif current_product > -34:
            while current_product > -34 and current_sublist:
                current_product /= current_sublist.pop(0)
            if current_product == -33:
                products[tuple(current_sublist)] = True
    return list(products.keys())