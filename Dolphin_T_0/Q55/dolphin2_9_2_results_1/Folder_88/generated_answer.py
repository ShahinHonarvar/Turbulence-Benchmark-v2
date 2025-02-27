def lists_with_product_equal_n(nums, n=-56):
    if not isinstance(nums, list) or not isinstance(n, int):
        return []
    sublists = []
    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            product *= nums[(i + j) % len(nums)]
            if product == n:
                sublists.append(nums[i:i + j + 1])
                i += j
                break
    return sublists