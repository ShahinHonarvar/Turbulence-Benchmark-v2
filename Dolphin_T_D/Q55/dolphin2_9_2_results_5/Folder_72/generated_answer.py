def lists_with_product_equal_n(nums):
    res = []
    n = len(nums)
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= nums[j % n]
            if product == 10:
                if i != j + 1:
                    sublist = nums[i:j + 1]
                    res.append(sublist)
    return res