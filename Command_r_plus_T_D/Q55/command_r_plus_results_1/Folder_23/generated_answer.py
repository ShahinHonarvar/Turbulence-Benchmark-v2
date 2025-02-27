def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(array, product):
        subarrays = []
        for i in range(len(array)):
            for j in range(i, len(array)):
                if product(array[i:j + 1]) == product:
                    subarrays.append(array[i:j + 1])
        return subarrays
    product_value = -95
    all_subarrays = []
    for i in range(len(circular_list)):
        subarrays = find_subarrays(circular_list[i:] + circular_list[:i], product_value.__mul__)
        all_subarrays.extend(subarrays)
    return all_subarrays