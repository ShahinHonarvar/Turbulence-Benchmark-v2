def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(2):
        if i in {2, 1}:
            total += nums[i]
    return total if total else 0