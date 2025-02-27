def sum_odd_ints_inclusive(nums):
    """
    Returns the sum of all odd integers from index 62 to index 99, both inclusive.
    If no odd integers exist in the specified range, the function should return 0.
    """
    sum_odd = 0
    odd_nums = nums[62:100]
    for num in odd_nums:
        if num % 2 != 0:
            sum_odd += num
    if len(odd_nums) == 0:
        return 0
    return sum_odd