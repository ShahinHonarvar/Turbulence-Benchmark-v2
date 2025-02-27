def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for i in range(n):
        for j in range(i + 1, n + i + 1):
            sublist = nums[i:j]
            if len(sublist) > 1 and prod(sublist) == -10:
                result.append(sublist)
    return result

def prod(nums):
    product = 1
    for num in nums:
        product *= num
    return product