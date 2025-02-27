def sum_ints_div_by_either_nums(nums):
    """Returns the sum of all integers divisible by either 15 or 87 from index 42 to index 43, both inclusive. If no such integers exist in the specified range, the function should return 0."""
    sum_div_nums = 0
    for num in nums[42:44]:
        if num % 15 == 0 or num % 87 == 0:
            sum_div_nums += num
    return sum_div_nums