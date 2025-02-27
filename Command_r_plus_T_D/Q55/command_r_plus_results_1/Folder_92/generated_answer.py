def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def get_subarrays(arr, product):
        subarrays = []
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if product(arr[i:j + 1]) == product:
                    subarrays.append(arr[i:j + 1])
        return subarrays

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    all_subarrays = []
    for i in range(len(circular_list)):
        subarray = circular_list[i:] + circular_list[:i]
        all_subarrays.extend(get_subarrays(subarray, 5))
    return all_subarrays