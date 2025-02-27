def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, target, n):
        count_map = {1: 1}
        product = 1
        left = 0
        for right in range(n):
            product *= arr[right]
            if product == target:
                count_map[right - left + 1] = count_map.get(right - left + 1, 0) + 1
            if product * arr[left] == target:
                count_map[right - left + 2] = count_map.get(right - left + 2, 0) + 1
            if product * arr[left] == target * arr[right + 1]:
                left = right + 1
        return count_map
    result = []
    n = len(circular_list)
    target = 51
    for i in range(n):
        subarray_counts = find_subarrays(circular_list, target, n)
        for j in range(i, i + max(subarray_counts.keys())):
            subarray = circular_list[j:j + subarray_counts[subarray_counts[1]]]
            if subarray_counts[len(subarray)] > 0:
                result.append(subarray)
                subarray_counts[len(subarray)] -= 1
    return result