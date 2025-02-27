def lists_with_product_equal_n(nums):
    sublists = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            product = 1
            for k in range(i, j):
                product *= nums[k % len(nums)]
            if product == -115:
                sublists.append(nums[i:j])
    return sublists