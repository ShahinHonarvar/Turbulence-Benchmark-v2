def lists_with_product_equal_n(nums):
    res = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            if prod(nums[i:j]) == -17:
                res.append(nums[i:j])
    return res

def prod(nums):
    p = 1
    for num in nums:
        p *= num
    return p