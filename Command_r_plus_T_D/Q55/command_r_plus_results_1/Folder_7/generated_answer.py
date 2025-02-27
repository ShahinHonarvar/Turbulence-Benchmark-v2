def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, target, n):
        count_map = {1: 1}
        product = 1
        res = []
        for num in arr:
            product *= num
            if product == target:
                res.append(arr[:])
            if product in count_map:
                res.extend([arr[i:i + n] for i in range(count_map[product], n)])
            if product * arr[n - 1] in count_map:
                count_map[product * arr[n - 1]] = count_map.get(product * arr[n - 1], 0) + 1
            count_map[product] = count_map.get(product, 0) + 1
        return res
    result = []
    for i in range(len(circular_list)):
        sublist = circular_list[i:] + circular_list[:i]
        result.extend(find_subarrays(sublist, 537, len(circular_list)))
    return result