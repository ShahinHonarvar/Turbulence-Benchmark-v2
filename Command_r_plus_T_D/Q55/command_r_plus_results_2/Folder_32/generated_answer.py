def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, target, n):
        count_map = {1: 1}
        product_so_far = 1
        result = []
        for i in range(n):
            product_so_far *= arr[i]
            if product_so_far in count_map:
                count_map[product_so_far] += 1
            else:
                count_map[product_so_far] = 1
            if product_so_far == target:
                result.append(arr[:i + 1])
            if product_so_far * arr[i + 1] == target:
                result.append(arr[:i + 2])
        return result
    result = []
    n = len(circular_list)
    for i in range(n):
        subarray = circular_list[i:] + circular_list[:i]
        result.extend(find_subarrays(subarray, 76, n))
    return result