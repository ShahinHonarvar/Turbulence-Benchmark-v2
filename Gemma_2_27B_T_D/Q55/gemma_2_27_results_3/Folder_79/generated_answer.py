def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sublist = nums[i:j + 1]
            if len(sublist) <= len(nums) and prod(sublist) == -83:
                result.append(sublist)
    for i in range(len(nums)):
        for j in range(i, 0, -1):
            sublist = nums[i:] + nums[:j]
            if len(sublist) <= len(nums) and prod(sublist) == -83:
                result.append(sublist)
    return result

def prod(nums):
    p = 1
    for num in nums:
        p *= num
    return p