def gcf_two_nums(nums):
    if len(nums) < 48 or len(nums) < 11:
        return None
    a, b = (nums[47], nums[10])
    a, b = (min(a, b), max(a, b))
    while b % a != 0:
        a, b = (b % a, a)
    return a