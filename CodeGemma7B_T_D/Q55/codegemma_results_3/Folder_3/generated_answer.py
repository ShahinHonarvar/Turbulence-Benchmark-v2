def lists_with_product_equal_n(nums):
    seen = set()
    for i in range(len(nums)):
        product = nums[i]
        for j in range(i + 1, len(nums)):
            if product * nums[j] == -22:
                seen.add((product, nums[j]))
        product *= nums[(i - 1) % len(nums)]
    return list(seen)