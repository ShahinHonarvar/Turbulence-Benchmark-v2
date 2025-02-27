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
                result.extend([arr[i:i + n] for i in range(count_map[product], n)])
            if product != 0:
                count_map[product] = n + 1
            n += 1
            arr.pop(0)
        return result
    result = []
    for i in range(len(circular_list)):
        temp_list = circular_list[i:] + circular_list[:i]
        result.extend(find_subarrays(temp_list, 10, 1))
    return result