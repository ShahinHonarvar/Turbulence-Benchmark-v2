def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sublist = nums[i:j + 1] + nums[:i] if j >= i else nums[i:]
            if len(sublist) > 0 and 28 == product(sublist):
                result.append(sublist)
    return result

def product(nums):
    prod = 1
    for num in nums:
        prod *= num
    return prod