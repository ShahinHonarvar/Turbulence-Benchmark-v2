def lists_with_product_equal_n(nums):
    if len(nums) == 0:
        return []
    n = len(nums)
    prefix = [1] + [0] * n
    suffix = [0] * n + [1]
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] * nums[i - 1]
        suffix[n - i] = suffix[n - i + 1] * nums[n - i]
    res = []
    for i in range(1, n + 1):
        product = prefix[i - 1] * suffix[i + 1]
        if product == -30 and i - 1 < n:
            res.append(nums[:i])
            res.append(nums[i:])
    return list(set(map(tuple, res)))