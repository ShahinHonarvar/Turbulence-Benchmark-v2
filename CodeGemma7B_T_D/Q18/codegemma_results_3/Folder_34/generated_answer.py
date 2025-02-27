def sum_ints_div_by_either_nums(nums):
    """takes a list of integers and returns the sum of all integers divisible by either 9 or 11 from index 60 to index 200, both inclusive. If no such integers exist in the specified range, the function should return 0."""
    return sum((num for num in nums[60:201] if num % 9 == 0 or num % 11 == 0))