def lists_with_product_equal_n(nums):
    n = 46
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + i + 1):
            if j < len(nums):
                product = 1
                for num in nums[i:j + 1]:
                    product *= num
                if product == n:
                    result.append(nums[i:j + 1])
            else:
                product = 1
                for num in nums[i:] + nums[:j % len(nums)]:
                    product *= num
                if product == n:
                    result.append(nums[i:] + nums[:j % len(nums)])
    return result