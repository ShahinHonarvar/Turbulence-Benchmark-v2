def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, product):
        subarrays = []
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if product(arr[i:j + 1]) == product:
                    subarrays.append(arr[i:j + 1])
        return subarrays
    products_equal_to_four = find_subarrays(circular_list, 4)
    products_equal_to_four.extend(find_subarrays(circular_list[1:], 4))
    return products_equal_to_four