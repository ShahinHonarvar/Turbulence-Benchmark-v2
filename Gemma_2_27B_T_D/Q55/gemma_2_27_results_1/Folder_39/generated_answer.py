def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + i + 1):
            sublist = nums[i:j % len(nums)]
            if prod(sublist) == -46:
                result.append(sublist)
    return result

def prod(nums):
    p = 1
    for num in nums:
        p *= num
    return p