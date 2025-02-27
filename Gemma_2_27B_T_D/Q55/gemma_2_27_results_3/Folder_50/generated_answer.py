def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sublist = nums[i:j + 1]
            product = 1
            for num in sublist:
                product *= num
            if product == 45:
                result.append(sublist)
            if j == len(nums) - 1:
                sublist = nums[i:] + nums[:j + 1]
                product = 1
                for num in sublist:
                    product *= num
                if product == 45:
                    result.append(sublist)
    return result