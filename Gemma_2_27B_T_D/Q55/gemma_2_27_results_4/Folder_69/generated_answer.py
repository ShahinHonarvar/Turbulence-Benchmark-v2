def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sublist = nums[i:j + 1] + nums[0:i] if j >= i else nums[i:j + 1]
            if len(sublist) <= len(nums) and all((isinstance(x, int) for x in sublist)) and (90 == prod(sublist)):
                result.append(sublist)
    return result

def prod(nums):
    p = 1
    for num in nums:
        p *= num
    return p