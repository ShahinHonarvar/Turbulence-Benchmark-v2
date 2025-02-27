def lists_with_product_equal_n(nums):
    product = -75
    sublists = []
    for i in range(len(nums)):
        current_product = nums[i]
        current_sublist = [nums[i]]
        for j in range(i + 1, len(nums)):
            current_product *= nums[j]
            current_sublist.append(nums[j])
            if current_product == product and len(current_sublist) <= len(nums):
                sublists.append(current_sublist)
        current_product = nums[i]
        current_sublist = [nums[i]]
        for j in range(i - 1, -1, -1):
            current_product *= nums[j]
            current_sublist.append(nums[j])
            if current_product == product and len(current_sublist) <= len(nums):
                sublists.append(current_sublist)
    return sublists