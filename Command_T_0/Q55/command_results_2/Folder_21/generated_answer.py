def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] * nums[j] * nums[k] == 851:
                    result.append(list(range(i, j + 1)))
                    result.append(list(range(j, k + 1)))
                    result.append(list(range(k, i + 1)))
    return result