def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(array, target_product, start, end):
        if start > end:
            return []
        if end - start + 1 < len(circular_list):
            return []
        if prod(array[start:end + 1]) == target_product:
            return [array[start:end + 1]]
        return find_subarrays(array, target_product, start + 1, end) + find_subarrays(array, target_product, start, end - 1)

    def prod(lst):
        p = 1
        for i in lst:
            p *= i
        return p
    subarrays = find_subarrays(circular_list, -56, 0, len(circular_list) - 1)
    return subarrays