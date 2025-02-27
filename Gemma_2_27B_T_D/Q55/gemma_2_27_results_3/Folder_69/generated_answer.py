def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sub_list = nums[i:j + 1]
            product = 1
            for num in sub_list:
                product *= num
            if product == 90:
                result.append(sub_list)
    return result