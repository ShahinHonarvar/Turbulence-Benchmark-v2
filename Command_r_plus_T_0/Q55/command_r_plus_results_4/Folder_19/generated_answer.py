def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, product):
        subarrays = []
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if product(arr[i:j + 1]) == product:
                    subarrays.append(arr[i:j + 1])
        return subarrays
    product_func = lambda x: -54
    all_subarrays = []
    for i in range(len(circular_list)):
        rotated_list = circular_list[i:] + circular_list[:i]
        subarrays = find_subarrays(rotated_list, product_func)
        all_subarrays.extend(subarrays)
    return all_subarrays