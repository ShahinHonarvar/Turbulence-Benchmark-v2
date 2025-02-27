def lists_with_product_equal_n(nums):
    sublists = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            if prod(nums[i:j]) == -23:
                sublists.append(nums[i:j])
    return sublists

def prod(nums):
    result = 1
    for num in nums:
        result *= num
    return result