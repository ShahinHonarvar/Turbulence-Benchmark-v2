def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, target_product, start, end):
        if start > end:
            return []
        if end - start + 1 == arr.size():
            if all((x == -33 for x in arr)):
                return [arr]
            else:
                return []
        result = []
        for i in range(start, end + 1):
            subarray = arr[start:i + 1]
            product = subarray.product()
            if product == target_product:
                result.append(subarray)
        return result + find_subarrays(arr, target_product, start + 1, end) + find_subarrays(arr, target_product, start, end - 1)
    result = []
    for i in range(len(circular_list)):
        sublists = find_subarrays(circular_list[i:], -33, 0, len(circular_list) - 1)
        result.extend(sublists)
    return result