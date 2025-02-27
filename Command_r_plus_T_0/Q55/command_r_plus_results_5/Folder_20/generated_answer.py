def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, target_product, start, end):
        if start > end:
            return []
        if end - start + 1 < len(arr):
            return []
        product_so_far = 1
        subarrays = []
        for i in range(start, end + 1):
            product_so_far *= arr[i % len(arr)]
            if product_so_far == target_product:
                subarrays.append(arr[start:i + 1])
            if product_so_far == target_product and arr[i % len(arr)] != 1:
                product_so_far = 1
                continue
        return subarrays
    subarrays = []
    for i in range(len(circular_list)):
        subarrays.extend(find_subarrays(circular_list, -69, i, i + len(circular_list) - 1))
    return subarrays