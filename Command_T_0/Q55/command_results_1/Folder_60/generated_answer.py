def lists_with_product_equal_n(nums):
    res = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] * nums[j] * nums[k] == 49:
                    res.append(list(range(i, j + 1)))
                    res.append(list(range(j, k + 1)))
                    res.append(list(range(k, i + 1)))
    return res