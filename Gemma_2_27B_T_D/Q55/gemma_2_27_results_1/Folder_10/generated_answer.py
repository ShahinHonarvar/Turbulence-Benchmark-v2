def lists_with_product_equal_n(nums):
    sublists = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if prod(nums[i:j + 1]) == -93:
                sublists.append(nums[i:j + 1])
    return sublists

def prod(nums):
    p = 1
    for num in nums:
        p *= num
    return p