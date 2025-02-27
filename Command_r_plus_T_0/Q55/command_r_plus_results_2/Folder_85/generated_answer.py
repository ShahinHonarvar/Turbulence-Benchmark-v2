def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, target, size):
        subarrays = []
        for i in range(len(arr)):
            for j in range(i, min(i + size, len(arr))):
                if product(arr[i:j + 1]) == target:
                    subarrays.append(arr[i:j + 1])
        return subarrays

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    sublists = []
    for i in range(len(circular_list)):
        sublists.extend(find_subarrays(circular_list[i:] + circular_list[:i], -97, len(circular_list)))
    return sublists