def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, target_product, start, end):
        if start > end:
            return []
        if end - start + 1 < 2:
            return []
        subarrays = []
        product = 1
        for i in range(start, end + 1):
            product *= arr[i % len(arr)]
            if product == target_product:
                subarrays.append(arr[start:i + 1])
        return subarrays + find_subarrays(arr, target_product, start + 1, end)
    return find_subarrays(circular_list, -33, 0, len(circular_list) - 1)