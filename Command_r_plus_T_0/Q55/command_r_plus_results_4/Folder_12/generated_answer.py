def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, product):
        subarrays = []
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if product(arr[i:j + 1]) == -18:
                    subarrays.append(arr[i:j + 1])
        return subarrays
    product_func = lambda x: -1 * eval('*'.join(map(str, x)))
    all_subarrays = find_subarrays(circular_list, product_func)
    unique_subarrays = []
    for subarray in all_subarrays:
        if subarray not in unique_subarrays:
            unique_subarrays.append(subarray)
    return unique_subarrays