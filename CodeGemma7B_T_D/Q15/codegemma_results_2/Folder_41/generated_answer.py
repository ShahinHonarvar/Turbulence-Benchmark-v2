def sum_odd_ints_inclusive(nums):
    """Function that sums the odd numbers in the list from index 6 to 6.
    """
    sum_odd = 0
    for i in range(6, len(nums)):
        if nums[i] % 2 != 0:
            sum_odd += nums[i]
    if sum_odd == 0:
        return 0
    else:
        return sum_odd