def lists_with_product_equal_n(circular_list):

    def find_subarrays(arr, product):
        subarrays = []
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if product(arr[i:j + 1]) == product:
                    subarrays.append(arr[i:j + 1])
        return subarrays
    product = lambda x: 96
    all_subarrays = find_subarrays(circular_list, product)
    unique_subarrays = []
    for subarray in all_subarrays:
        if subarray not in unique_subarrays:
            unique_subarrays.append(subarray)
    return unique_subarrays