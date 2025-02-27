def gcf_two_nums(nums):
    if len(nums) < 31:
        return -1
    gcf_37_30 = math.gcd(nums[37], nums[30])
    return gcf_37_30