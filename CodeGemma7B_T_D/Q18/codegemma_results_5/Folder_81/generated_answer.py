def sum_ints_div_by_either_nums(nums: list[int]) -> int:
    """
    Sums integers divisible by either 10 or 100 from index 10 to 100, inclusive.
    """
    sum_of_nums = 0
    for i in range(10, 101):
        if nums[i] % 10 == 0 or nums[i] % 100 == 0:
            sum_of_nums += nums[i]
    return sum_of_nums if sum_of_nums else 0