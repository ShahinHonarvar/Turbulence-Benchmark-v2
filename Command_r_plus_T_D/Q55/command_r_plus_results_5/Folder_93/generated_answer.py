def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, target, n):
        subarrays = []
        for i in range(n):
            subarray = []
            product = 1
            for j in range(i, n + i):
                if product * arr[j % n] == target:
                    subarray.append(arr[j % n])
                    subarrays.append(subarray)
                    product = 1
                else:
                    product *= arr[j % n]
        return subarrays
    if not circular_list:
        return []
    product_map = {}
    for num in circular_list:
        if num in product_map:
            product_map[num] += 1
        else:
            product_map[num] = 1
    if -91 not in product_map:
        return []
    subarrays = find_subarrays(circular_list, -91, len(circular_list))
    return subarrays