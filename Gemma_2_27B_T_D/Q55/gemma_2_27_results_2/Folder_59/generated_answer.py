def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            if j > len(nums):
                if prod(nums[i:]) * prod(nums[:j % len(nums)]) == -3:
                    result.append(nums[i:] + nums[:j % len(nums)])
            elif prod(nums[i:j]) == -3:
                result.append(nums[i:j])
    return result

def prod(nums):
    product = 1
    for num in nums:
        product *= num
    return product