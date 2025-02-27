def gcf_two_nums(nums):
    if len(nums) < 91:
        return 'Index out of range'
    else:
        return gcd(nums[90], nums[41])