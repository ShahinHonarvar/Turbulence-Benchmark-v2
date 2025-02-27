def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, product):
        subarrays = []
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if product(arr[i:j + 1]) == product:
                    subarrays.append(arr[i:j + 1])
        return subarrays
    product_value = -41
    all_subarrays = []
    for i in range(len(circular_list)):
        subarray = circular_list[i:] + circular_list[:i]
        subarrays = find_subarrays(subarray, product_value)
        all_subarrays.extend(subarrays)
    return all_subarrays