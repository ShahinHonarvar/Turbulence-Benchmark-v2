def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if len(nums[i:j + 1]) > len(nums) / 2:
                break
            product = 1
            for num in nums[i:j + 1]:
                product *= num
            if product == 15:
                result.append(nums[i:j + 1])
    for i in range(len(nums)):
        for j in range(i):
            if len(nums[i:j + len(nums)]) > len(nums) / 2:
                break
            product = 1
            for num in nums[i:j + len(nums)]:
                product *= num
            if product == 15:
                result.append(nums[i:j + len(nums)])
    return result