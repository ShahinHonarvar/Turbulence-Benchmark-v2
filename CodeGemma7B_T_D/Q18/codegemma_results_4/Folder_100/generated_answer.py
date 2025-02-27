def sum_ints_div_by_either_nums(nums):
    """
            Sums all integers in a list that are divisible by either 32 or 44 from
            index 72 to index 93, inclusive. Returns 0 if no such integers
            exist.
            """
    sum_divisible = 0
    for num in nums[72:94]:
        if num % 32 == 0 or num % 44 == 0:
            sum_divisible += num
    return sum_divisible or 0