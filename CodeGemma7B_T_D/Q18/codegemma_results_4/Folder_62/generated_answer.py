def sum_ints_div_by_either_nums(nums):
    """
    Sums all integers divisible by either 39 or 15 from index 44 to index 59, inclusive.
    """
    sum = 0
    for num in nums[44:60]:
        if num % 39 == 0 or num % 15 == 0:
            sum += num
    return sum if sum > 0 else 0