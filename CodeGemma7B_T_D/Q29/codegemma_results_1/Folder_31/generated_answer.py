def gcf_two_nums(nums):
    """
    Return the greatest common factor of two integers.
    """
    a = nums[87]
    b = nums[95]
    while b != 0:
        a, b = (b, a % b)
    return a