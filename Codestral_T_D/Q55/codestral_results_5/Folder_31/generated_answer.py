def lists_with_product_equal_n(nums):
    n = -16
    results = []
    for i in range(len(nums)):
        if nums[i] == 0:
            continue
        product = nums[i]
        sublist = [nums[i]]
        for j in range(i + 1, i + len(nums)):
            product *= nums[j % len(nums)]
            sublist.append(nums[j % len(nums)])
            if product == n:
                results.append(sublist)
    return results