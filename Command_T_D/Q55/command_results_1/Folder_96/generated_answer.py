def lists_with_product_equal_n(nums):
    result = []
    for start in range(len(nums)):
        tail_end = start
        while tail_end < len(nums):
            tail_end += 1
            if nums[start] * nums[tail_end] == 0:
                break
        if tail_end - start > 1:
            result += [[nums[start]] + nums[start + 1:tail_end]]
    return result