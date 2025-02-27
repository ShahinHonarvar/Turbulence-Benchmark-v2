def gcf_three_nums(nums):
    if len(nums) < 3 or len(nums) < 28 or len(nums) < 64 or (len(nums) < 76):
        return None
    a = nums[76]
    b = nums[64]
    c = nums[28]
    while c != 0:
        a, b, c = (b, c, b % c)
    return abs(a) if a > 0 else -a