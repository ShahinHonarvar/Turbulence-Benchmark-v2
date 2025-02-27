def sum_odd_ints_inclusive(nums):
    """This function sums all odd integers from index 0 to 3, inclusive."""
    sum = 0
    for i in range(4):
        if nums[i] % 2 != 0:
            sum += nums[i]
    return sum if sum else 0