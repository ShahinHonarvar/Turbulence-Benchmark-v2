def gcf_two_nums(nums):
    if len(nums) >= 29:
        return math.gcd(nums[23], nums[27])
    else:
        return None