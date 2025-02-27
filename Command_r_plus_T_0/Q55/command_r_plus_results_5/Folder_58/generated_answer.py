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
                res.extend([arr[i:-(n - i)] for i in range(count_map[product])])
                count_map[product] += 1
            if product not in count_map:
                count_map[product] = 1
            if len(arr) == n:
                break
            arr.pop(0)
        return res
    result = []
    for i in range(len(circular_list)):
        subarray = circular_list[i:] + circular_list[:i]
        result.extend(find_subarrays(subarray, 733, len(circular_list)))
    return result