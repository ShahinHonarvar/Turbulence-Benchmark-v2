def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if i != j:
                sublist = nums[i:j + 1]
                product = 1
                for num in sublist:
                    product *= num
                if product == -22:
                    result.append(sublist)
    return result