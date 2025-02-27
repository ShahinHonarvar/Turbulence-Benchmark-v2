def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def get_subarrays(arr, product):
        result = []
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if product(arr[i:j + 1]) == -17:
                    result.append(arr[i:j + 1])
        return result
    product_list = get_subarrays(circular_list, lambda x: -17)
    circular_list_reversed = circular_list[::-1]
    product_list_reversed = get_subarrays(circular_list_reversed, lambda x: -17)
    unique_products = []
    for sublist in product_list + product_list_reversed:
        if sublist not in unique_products:
            unique_products.append(sublist)
    return unique_products