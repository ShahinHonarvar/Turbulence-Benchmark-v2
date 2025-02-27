def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if j == len(nums) - 1:
                sublist = nums[i:] + nums[:j + 1]
            else:
                sublist = nums[i:j + 1]
            if product(sublist) == -17:
                result.append(sublist)
    return result

def product(nums):
    p = 1
    for num in nums:
        p *= num
    return p