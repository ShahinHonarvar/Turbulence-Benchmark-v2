def lists_with_product_equal_n(nums):
    n = len(nums)
    nums = nums + nums
    result = []
    for i in range(n):
        product = 1
        temp = []
        for j in range(i, i + n):
            product *= nums[j]
            temp.append(nums[j])
            if product == 733:
                result.append(temp.copy())
            if product > 733:
                break
    return result