def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for i in range(n):
        for j in range(i, n):
            if len(nums[i:j + 1]) == 1:
                if nums[i] == -23:
                    result.append([nums[i]])
            else:
                product = 1
                for k in range(i, j + 1):
                    product *= nums[k]
                if product == -23:
                    result.append(nums[i:j + 1])
    return result