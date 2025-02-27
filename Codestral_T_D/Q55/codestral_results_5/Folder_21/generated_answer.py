def lists_with_product_equal_n(nums):
    n = 851
    result = []
    for i in range(len(nums)):
        prod = 1
        sublist = []
        for j in range(i, len(nums) + i):
            prod *= nums[j % len(nums)]
            sublist.append(nums[j % len(nums)])
            if prod == n:
                result.append(sublist)
            elif prod > n:
                break
    return result