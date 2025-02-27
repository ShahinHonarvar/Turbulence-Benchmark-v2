def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(lst, target_product):
        length = len(lst)
        left = 0
        curr_product = 1
        result = []
        for right in range(length):
            curr_product *= lst[right]
            while curr_product == target_product or curr_product % target_product == 0:
                result.append(lst[left:right + 1])
                curr_product /= lst[left]
                left += 1
        return result
    product_of_minus_26 = [-1, -26, 1, 26, -13, 2, 13]
    return find_subarrays(circular_list, -26)