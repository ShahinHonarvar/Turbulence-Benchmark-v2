def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, product):
        subarrays = []
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if product == 1:
                    subarrays.append(arr[i:j + 1])
                elif product == arr[i] * arr[j]:
                    subarrays.append(arr[i:j + 1])
        return subarrays
    result = []
    for i in range(len(circular_list)):
        subarray = circular_list[i:] + circular_list[:i]
        result.extend(find_subarrays(subarray, 51))
    return result