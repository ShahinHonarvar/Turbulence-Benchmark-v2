def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, target_product, start, end):
        if start > end:
            return []
        if end - start + 1 == len(arr) and target_product == 1:
            return [arr]
        subarrays = []
        for i in range(start, end + 1):
            product = 1
            for j in range(i, end + 1):
                product *= arr[j % len(arr)]
                if product == target_product:
                    subarrays.append(arr[i % len(arr):j + 1])
        return subarrays
    target_product = -76
    sublists = []
    for i in range(len(circular_list)):
        subarrays = find_subarrays(circular_list, target_product, i, i + len(circular_list) - 1)
        sublists.extend(subarrays)
    return sublists