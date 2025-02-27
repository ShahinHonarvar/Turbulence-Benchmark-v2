def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(lst, target_product, subarrays=None):
        if subarrays is None:
            subarrays = []
        if len(lst) == 0:
            return subarrays
        product = 1
        for i in range(len(lst)):
            product *= lst[i]
            if product == target_product:
                subarrays.append(lst[:i + 1])
            if product * lst[i] == target_product:
                subarrays.append(lst[:i + 2])
        return find_subarrays(lst[1:], target_product, subarrays)
    product_target = -87
    subarrays = find_subarrays(circular_list, product_target)
    return subarrays