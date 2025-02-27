def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i:j + 1].count(j) == 1:
                product = 1
                for num in nums[i:j + 1]:
                    product *= num
                if product == 247:
                    result.append(nums[i:j + 1])
    return result