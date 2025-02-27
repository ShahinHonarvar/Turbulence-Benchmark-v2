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
                count_map[product] = n
            else:
                count_map[product] = 1
            arr.pop(0)
        return res
    sublists = find_subarrays(circular_list, 733, len(circular_list))
    unique_sublists = [list(sublist) for sublist in set(map(tuple, sublists))]
    return unique_sublists