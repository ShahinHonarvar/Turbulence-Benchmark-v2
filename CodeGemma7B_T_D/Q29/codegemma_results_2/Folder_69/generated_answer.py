def gcf_two_nums(nums) -> int:
    """Return the greatest common factor of two integers."""
    a, b = (nums[894], nums[801])
    if a % b == 0:
        return b
    while a % b != 0:
        a, b = (b, a % b)
    return b