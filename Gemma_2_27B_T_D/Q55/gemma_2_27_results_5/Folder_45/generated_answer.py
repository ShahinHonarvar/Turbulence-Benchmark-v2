def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sublist = nums[i:j + 1] + nums[:i] if j >= i else nums[i:]
            if len(sublist) > 0 and prod(sublist) == -5:
                result.append(sublist)
    return result

def prod(nums):
    p = 1
    for num in nums:
        p *= num
    return p