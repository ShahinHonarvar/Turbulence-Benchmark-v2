def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, target_product, start, end):
        product = 1
        subarrays = []
        for i in range(start, end + 1):
            product *= arr[i]
            if product == target_product:
                subarrays.append(arr[start:i + 1])
        return subarrays
    target_product = -69
    sublists = []
    for i in range(len(circular_list)):
        subarrays = find_subarrays(circular_list, target_product, i, i + len(circular_list) - 1)
        sublists.extend(subarrays)
    return sublists