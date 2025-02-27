def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(lst, target_product, subarray=[]):
        if not lst:
            if target_product == 1:
                return [subarray]
            else:
                return []
        else:
            current_product = target_product / lst[0]
            return find_subarrays(lst[1:], current_product, subarray + [lst[0]]) + find_subarrays(lst[1:], target_product, subarray)
    product = -938
    sublists = []
    for i in range(len(circular_list)):
        subarray = circular_list[i:] + circular_list[:i]
        sublists_with_product = find_subarrays(subarray, product)
        sublists.extend(sublists_with_product)
    return sublists