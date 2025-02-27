def sum_ints_div_by_either_nums(nums):
    """Sum the integers in the list that are divisible by either 10 or 100 from index 0 to index 9, both inclusive."""
    sum_nums = 0
    for num in nums:
        if num in range(10, 101) and num % 10 == 0 or num % 100 == 0:
            sum_nums += num
    return 0 if sum_nums == 0 else sum_nums