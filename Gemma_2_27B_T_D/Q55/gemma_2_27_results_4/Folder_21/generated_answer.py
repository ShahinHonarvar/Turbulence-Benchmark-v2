def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if len(nums[i:j + 1]) > len(nums) / 2:
                break
            product = 1
            for num in nums[i:j + 1]:
                product *= num
            if product == 851:
                result.append(nums[i:j + 1])
    return result