def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def get_sublist_products(circular_list):
        products = []
        product = 1
        for num in circular_list:
            product *= num
            products.append(product)
        return products

    def find_subarrays(products, target_product):
        subarrays = []
        for i in range(len(products)):
            for j in range(i, len(products)):
                if products[j] % target_product == 0 and products[i] * (products[j] // target_product) == products[j]:
                    subarrays.append(circular_list[i:j + 1])
        return subarrays
    target_product = -72
    products = get_sublist_products(circular_list)
    sublists = find_subarrays(products, target_product)
    return sublists