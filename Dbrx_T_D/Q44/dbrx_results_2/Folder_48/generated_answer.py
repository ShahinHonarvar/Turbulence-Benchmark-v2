def composite_nums_between_indices(nums):
    composite_set = set()
    for i in range(len(nums)):
        if i >= 661 and i <= 924:
            n = nums[i]
            if n > 1 and (not all((n % j == 0 for j in range(2, n)))):
                composite_set.add(n)
    return composite_set if len(composite_set) > 0 else {}