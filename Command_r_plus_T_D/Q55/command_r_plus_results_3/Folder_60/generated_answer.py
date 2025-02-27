def lists_with_product_equal_n(circular_list):

    def get_sublist_products(lst):
        products = []
        product = 1
        for num in lst:
            product *= num
            products.append(product)
        return products
    result = []
    for i in range(len(circular_list)):
        sublist_products = get_sublist_products(circular_list[i:] + circular_list[:i])
        sublists = [circular_list[i:j] + circular_list[:i] for i in range(len(circular_list)) for j in range(i + 1, len(circular_list) + i + 1) if sublist_products[j - 1] == 49]
        result.extend(sublists)
    return result