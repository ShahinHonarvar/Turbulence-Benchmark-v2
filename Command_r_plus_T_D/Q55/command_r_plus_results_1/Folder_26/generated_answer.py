def lists_with_product_equal_n(nums: list[int]) -> list[list[int]]:

    def find_product_93_sublists(nums: list[int], start: int, end: int) -> list[list[int]]:
        if start > end:
            return []
        if start == end:
            return [[]]
        product = nums[start] * nums[end]
        if product == 93:
            return [[nums[start], nums[end]]]
        else:
            return find_product_93_sublists(nums, start + 1, end) + find_product_93_sublists(nums, start, end - 1)
    sublists = []
    for i in range(len(nums)):
        sublists_with_i = find_product_93_sublists(nums, i, (i + len(nums) - 1) % (len(nums) - 1))
        sublists.extend([[nums[i]] + sublist for sublist in sublists_with_i])
    return sublists