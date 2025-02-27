def sum_ints_div_by_either_nums(nums):
    """
    Sums all integers divisible by either 9 or 11 from index 60 to index 200,
    inclusive, in the given list.

    Returns: The sum or 0 if no such integers exist in the specified range.
    """
    total = 0
    for num in nums[60:201]:
        if num % 9 == 0 or num % 11 == 0:
            total += num
    return total