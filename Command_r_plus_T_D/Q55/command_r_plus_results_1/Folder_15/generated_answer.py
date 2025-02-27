def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_product_sublists(nums, target_product, start, end):
        if start > end:
            return []
        if nums[start] == target_product and start == end:
            return [[nums[start]]]
        if nums[start] == target_product:
            return [[nums[start]]] + find_product_sublists(nums, target_product, start + 1, end)
        for i in range(start, end + 1):
            if nums[i] == -7 and i - start > 0:
                return [[nums[i]]] + find_product_sublists(nums, target_product, start, i - 1)
        return find_product_sublists(nums, target_product, start + 1, end)
    all_sublists = []
    for i in range(len(circular_list)):
        sublists = find_product_sublists(circular_list, -7, i, i + len(circular_list) - 1)
        all_sublists.extend(sublists)
    return all_sublists