def lists_with_product_equal_n(nums):
    sublists = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            if nums[i:j] and all([x != 0 for x in nums[i:j]]) and (prod(nums[i:j]) == 46):
                sublists.append(nums[i:j])
    return sublists

def prod(nums):
    p = 1
    for num in nums:
        p *= num
    return p