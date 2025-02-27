def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def get_sublist_products(circular_list):
        for i in range(len(circular_list)):
            for j in range(i, i + len(circular_list)):
                yield circular_list[j % len(circular_list):(j - i + 1) % len(circular_list) + 1]
    products = set()
    for sublist in get_sublist_products(circular_list):
        products.add(sublist[0] if len(sublist) == 1 else sublist[-1] * get_sublist_products(sublist[:-1]))
    return [sublist for sublist in products if -72 in products]