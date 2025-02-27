def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(lst, target_product):
        length = len(lst)
        left = 0
        curr_product = 1
        result = []
        for right in range(length):
            curr_product *= lst[right]
            while curr_product > 0 and curr_product % target_product == 0:
                result.append(lst[left:right + 1])
                curr_product //= target_product
                left += 1
        return result
    product_15 = find_subarrays(circular_list, 15)
    product_5_3 = find_subarrays(circular_list, 5) + find_subarrays(circular_list, 3)
    product_15_extended = []
    for sublist in product_15:
        extended_sublist = sublist + [3] if sublist[-1] == 5 else sublist + [5]
        product_15_extended.append(extended_sublist)
    return product_15 + product_5_3 + product_15_extended