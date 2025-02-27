def sum_odd_ints_inclusive(nums):
    """Sum of odd integers from index 3 to index 5, inclusive."""
    sum = 0
    for num in nums[3:6]:
        if num % 2 != 0:
            sum += num
    return sum or 0