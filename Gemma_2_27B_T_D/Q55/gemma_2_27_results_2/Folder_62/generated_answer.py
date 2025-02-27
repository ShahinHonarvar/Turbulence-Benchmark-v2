def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for i in range(n):
        for j in range(i + 1, n + i + 1):
            if all((num != 0 for num in nums[i:j % n])):
                product = 1
                for k in range(i, j % n):
                    product *= nums[k]
                if product == 100:
                    result.append(nums[i:j % n])
    return result