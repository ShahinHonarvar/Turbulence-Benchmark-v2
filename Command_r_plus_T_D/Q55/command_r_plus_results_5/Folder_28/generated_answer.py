def lists_with_product_equal_n(nums: list[int]) -> list[list[int]]:

    def find_product_sublists(nums, target_product, start, end):
        product = 1
        sublists = []
        for i in range(start, end + 1):
            product *= nums[i % len(nums)]
            if product == target_product:
                sublists.append(nums[start:i + 1])
        return sublists
    sublists = []
    for i in range(len(nums)):
        sublists.extend(find_product_sublists(nums, 85, i, i + len(nums) - 1))
    return sublists