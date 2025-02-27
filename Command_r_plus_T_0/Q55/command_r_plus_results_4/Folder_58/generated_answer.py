def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, target, n):
        count_map = {1: 1}
        product = 1
        res = []
        for i in range(n):
            product *= arr[i]
            if product == target:
                res.append(arr[:i + 1])
            if product in count_map:
                res.extend([arr[j:i + 1] for j in count_map[product]])
                count_map[product] += 1
            else:
                count_map[product] = 1
        return res
    sublists = find_subarrays(circular_list, 733, len(circular_list))
    circular_sublist = circular_list + circular_list
    sublists.extend(find_subarrays(circular_sublist, 733, len(circular_sublist)))
    return sublists