def lists_with_product_equal_n(nums):
    res = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if j != len(nums) - 1:
                product = nums[i]
                sub_list = [nums[i]]
                for k in range(i + 1, j + 1):
                    product *= nums[k]
                    sub_list.append(nums[k])
                if product == -83:
                    res.append(sub_list)
            else:
                product = nums[i]
                sub_list = [nums[i]]
                for k in range(i + 1, len(nums)):
                    product *= nums[k]
                    sub_list.append(nums[k])
                product *= nums[0]
                sub_list.append(nums[0])
                if product == -83:
                    res.append(sub_list)
    return res