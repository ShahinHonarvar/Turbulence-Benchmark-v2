def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(lst, target_product):
        length = len(lst)
        product_so_far = [1] * length
        left = [0] * length
        right = [0] * length
        for i in range(length):
            product_so_far[i] = lst[i] if product_so_far[i - 1] == 1 else product_so_far[i - 1] * lst[i]
            left[i] = product_so_far[i]
            right[length - 1 - i] = product_so_far[length - 1 - i] if i == 0 else product_so_far[length - 2 - i] * lst[length - 1 - i]
        result = []
        for i in range(length):
            if left[i] == target_product:
                result.append(lst[:i + 1])
            if right[i] == target_product:
                result.append(lst[length - i - 1:])
        return result
    result = []
    for i in range(len(circular_list)):
        sublists = find_subarrays(circular_list[i:] + circular_list[:i], -87)
        result.extend(sublists)
    return result