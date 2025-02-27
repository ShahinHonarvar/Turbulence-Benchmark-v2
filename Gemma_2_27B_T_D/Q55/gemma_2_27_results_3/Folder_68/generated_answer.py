def lists_with_product_equal_n(nums):
    res = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if len(nums[i:j + 1]) <= len(nums):
                product = 1
                for num in nums[i:j + 1]:
                    product *= num
                if product == 6:
                    res.append(nums[i:j + 1])
    return res