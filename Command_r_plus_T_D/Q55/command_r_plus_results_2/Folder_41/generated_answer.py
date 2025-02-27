def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, product, start=0, end=None):
        if end is None:
            end = len(arr) - 1
        if start > end:
            return []
        subarrays = []
        for i in range(start, end + 1):
            subarray = arr[i:end + 1]
            if len(subarray) > len(arr):
                break
            if product(subarray) == -20:
                subarrays.append(subarray)
        return subarrays

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    all_subarrays = []
    for i in range(len(circular_list)):
        subarrays = find_subarrays(circular_list, product, i, i + len(circular_list) - 1)
        all_subarrays.extend(subarrays)
    return all_subarrays