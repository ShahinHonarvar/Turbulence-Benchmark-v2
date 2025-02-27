def sum_odd_ints_inclusive(nums):
    """
    Sums of all odd integers from index 60 to index 200 (inclusive) in a given list.
    If no odd integers exist in the specified range, the function returns 0.
    """
    sum_odd = 0
    for i in range(60, 201):
        if i % 2 != 0:
            sum_odd += nums[i]
    return sum_odd if sum_odd else 0