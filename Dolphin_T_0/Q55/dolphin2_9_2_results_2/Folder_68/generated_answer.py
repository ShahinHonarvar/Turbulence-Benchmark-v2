def lists_with_product_equal_n(nums):
    result = []
    n = len(nums)
    for i in range(n):
        k = 1
        temp = []
        for j in range(i, i + n):
            temp.append(nums[j % n])
            if k * nums[j % n] > 6 or (k == 1 and nums[j % n] > 1):
                break
            k *= nums[j % n]
            if k == 6:
                result.append(temp[:])
    return result