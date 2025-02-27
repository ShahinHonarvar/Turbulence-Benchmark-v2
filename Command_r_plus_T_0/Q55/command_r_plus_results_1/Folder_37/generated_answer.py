def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, target, n):
        count_map = {1: 1}
        product = 1
        result = []
        for num in arr:
            product *= num
            if product == target:
                result.append(arr[:])
            if product in count_map:
                result.extend([arr[i:j] for i in range(len(arr)) for j in range(i + 1, len(arr) + 1) if j - i == n])
            count_map[product] = count_map.get(product, 0) + 1
        return result
    subarrays = find_subarrays(circular_list, -76, len(circular_list))
    circular_subarrays = []
    for subarray in subarrays:
        circular_subarrays.append(subarray + subarray[:1])
    return circular_subarrays