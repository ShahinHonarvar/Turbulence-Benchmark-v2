def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, target, n):
        count_map = {1: 1}
        product_so_far = 1
        for i in range(n):
            product_so_far *= arr[i]
            if product_so_far in count_map:
                count_map[product_so_far] += 1
            else:
                count_map[product_so_far] = 1
        product_so_far = 1
        for i in range(n):
            product_so_far *= arr[n - i - 1]
            if target % product_so_far == 0 and count_map.get(target // product_so_far, 0) > 0:
                yield arr[n - i:n]
    result = []
    for i in range(len(circular_list)):
        subarrays = list(find_subarrays(circular_list, 28, len(circular_list)))
        if subarrays:
            result.extend(subarrays)
    return result