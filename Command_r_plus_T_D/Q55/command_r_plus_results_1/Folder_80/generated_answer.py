def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, target, size):
        subarrays = []
        for i in range(len(arr)):
            for j in range(i, min(i + size, len(arr))):
                if prod(arr[i:j + 1]) == target:
                    subarrays.append(arr[i:j + 1])
        return subarrays

    def prod(lst):
        product = 1
        for num in lst:
            product *= num
        return product
    subarrays = find_subarrays(circular_list, 43, len(circular_list))
    return subarrays