def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, target_product, start, end):
        if start > end:
            return []
        if end - start + 1 < len(arr):
            return []
        product_so_far = 1
        for i in range(start, end + 1):
            product_so_far *= arr[i % len(arr)]
            if product_so_far == target_product:
                yield arr[start:i + 1]
            if product_so_far > target_product:
                break
    target_product = 76
    sublists = []
    for i in range(len(circular_list)):
        subarrays = list(find_subarrays(circular_list, target_product, i, i + len(circular_list) - 1))
        sublists.extend(subarrays)
    return sublists