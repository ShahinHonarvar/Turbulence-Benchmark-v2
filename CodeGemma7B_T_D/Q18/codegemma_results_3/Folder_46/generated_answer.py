def sum_ints_div_by_either_nums(nums):
    """
    Sums all integers in a list divisible by either 55 or 36 from index 11 to index 46 (inclusive).
    """
    sum = 0
    for i in range(11, 47):
        if nums[i] % 55 == 0 or nums[i] % 36 == 0:
            sum += nums[i]
    return sum or 0