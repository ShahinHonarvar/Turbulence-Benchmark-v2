def lists_with_product_equal_n(nums):
    n = 990
    result = []
    for i in range(len(nums)):
        current_product = 1
        current_list = []
        for j in range(i, len(nums)):
            current_product *= nums[j]
            current_list.append(nums[j])
            if current_product == n:
                result.append(current_list.copy())
            elif current_product > n:
                break
    return result