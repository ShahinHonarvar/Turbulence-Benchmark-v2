def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, target_product):
        length = len(arr)
        left, right = ([0] * length, [length] * length)
        product = [1] * length
        for i in range(length):
            product[i] = product[i - 1] * arr[i - 1] if i else 1
        for i in range(length):
            if arr[i] == target_product // 1:
                left[i] = max(0, i - 1)
            if product[i] % target_product == 0 and arr[i] == product[i] // target_product:
                right[i] = min(length, i + 1)
        return [arr[left[i]:right[i]] for i in range(length) if left[i] != right[i]]
    subarrays = find_subarrays(circular_list, -7)
    subarrays_with_duplicates = []
    for subarray in subarrays:
        circular_subarray = subarray + subarray
        subarrays_with_duplicates.extend([circular_subarray[i:i + len(circular_list)] for i in range(len(circular_list))])
    return subarrays_with_duplicates