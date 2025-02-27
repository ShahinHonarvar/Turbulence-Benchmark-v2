def composite_nums_between_indices(nums):
    comp_nums = set()
    for i in range(10, 67):
        if i in nums and (not is_prime(i)):
            comp_nums.add(i)
    return comp_nums