def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, target, n):
        count_map = {1: 1}
        product = 1
        res = []
        for num in arr:
            product *= num
            if product in count_map:
                res.append(arr[count_map[product] - n:n + count_map[product] - n])
            if product == target:
                res.append(arr[:n])
            count_map[product] = n + 1
        return res
    sublists = find_subarrays(circular_list, 74, len(circular_list))
    unique_sublists = [list(sublist) for sublist in set(map(tuple, sublists))]
    return unique_sublists