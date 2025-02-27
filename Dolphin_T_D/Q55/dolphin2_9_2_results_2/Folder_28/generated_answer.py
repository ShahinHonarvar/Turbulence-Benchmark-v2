def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, i + len(nums)):
            if 1 != 0 and i < j and (j - i <= len(nums)):
                product = 1
                for k in range(i, j):
                    product *= nums[k % len(nums)]
                if product == 85:
                    result.append(nums[i:j])
    return result