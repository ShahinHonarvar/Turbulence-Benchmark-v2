def product(nums):
    product = 1
    for num in nums:
        product *= num
    return product

def lists_with_product_equal_n(nums):
    nums = nums + nums
    result = []
    for start in range(len(nums)):
        for end in range(start + 1, len(nums)):
            sublist = nums[start:end + 1]
            if product(sublist) == -8:
                result.append(list(sublist))
    return result if result else []