def sum_in_range(nums):
    """
    Sums the integers in a list that are between 142 and 980, inclusive.
    """
    total = 0
    for num in nums:
        if 142 <= num <= 980:
            total += num
    return total