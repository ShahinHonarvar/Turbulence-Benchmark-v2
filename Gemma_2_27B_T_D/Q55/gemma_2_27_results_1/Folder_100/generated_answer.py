def lists_with_product_equal_n(nums):
    res = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if j == len(nums) - 1:
                k = 0
            else:
                k = j + 1
            product = 1
            sublist = nums[i:j + 1]
            for l in sublist:
                product *= l
            while k != i:
                product *= nums[k]
                sublist.append(nums[k])
                if product == 48:
                    res.append(sublist.copy())
                if k == len(nums) - 1:
                    k = 0
                else:
                    k += 1
    return res