def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, target, size):
        subarrays = []
        for i in range(len(arr)):
            product = 1
            for j in range(i, min(i + size, len(arr))):
                product *= arr[j]
                if product == target:
                    subarrays.append(arr[i:j + 1])
        return subarrays
    sublists = []
    for i in range(len(circular_list)):
        sublists.extend(find_subarrays(circular_list[i:], 247, len(circular_list)))
    return sublists