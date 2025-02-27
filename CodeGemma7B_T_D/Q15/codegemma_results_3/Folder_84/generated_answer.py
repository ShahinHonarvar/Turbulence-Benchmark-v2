def sum_odd_ints_inclusive(nums):
    """Given a list of integers, return the sum of all odd integers from index 43 to index 86, both inclusive. If no odd integers exist in the specified range, return 0."""
    total_sum = 0
    for num in nums[43:87]:
        if num % 2 != 0:
            total_sum += num
    if total_sum == 0:
        return 0
    else:
        return total_sum