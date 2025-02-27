def lists_with_product_equal_n(nums):
    n = -30
    sublists = []
    current_product = 1
    start_index = 0
    for i in range(len(nums)):
        current_product *= nums[i]
        while current_product > n and start_index < i:
            current_product /= nums[start_index]
            start_index += 1
        if current_product == n:
            sublists.append(nums[start_index:i + 1])
        if i == len(nums) - 1 and current_product != n:
            current_product = 1
            start_index = i + 1
    return sublists