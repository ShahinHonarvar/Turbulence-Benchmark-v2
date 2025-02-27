def gcf_three_nums(nums):
    if len(nums) < 54:
        return 'List is not long enough'
    return math.gcd(nums[53], math.gcd(nums[23], nums[45]))