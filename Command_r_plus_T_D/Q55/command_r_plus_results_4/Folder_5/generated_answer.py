def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(lst, target_product, n):
        result = []
        for i in range(len(lst)):
            for j in range(i, min(i + n, len(lst))):
                if product(lst[i:j + 1]) == target_product:
                    result.append(lst[i:j + 1])
        return result

    def product(lst):
        p = 1
        for num in lst:
            p *= num
        return p
    subarrays = find_subarrays(circular_list, -33, len(circular_list))
    unique_subarrays = []
    for subarray in subarrays:
        if subarray not in unique_subarrays:
            unique_subarrays.append(subarray)
    return unique_subarrays