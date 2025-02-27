def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(array, product):
        subarrays = []
        for i in range(len(array)):
            for j in range(i, len(array)):
                if product(array[i:j + 1]) == product:
                    subarrays.append(array[i:j + 1])
        return subarrays
    products = find_subarrays(circular_list, -9)
    products_in_circular_list = []
    for product in products:
        circular_product = product + product[1:]
        if set(product) == set(circular_product):
            products_in_circular_list.append(circular_product)
    return products_in_circular_list