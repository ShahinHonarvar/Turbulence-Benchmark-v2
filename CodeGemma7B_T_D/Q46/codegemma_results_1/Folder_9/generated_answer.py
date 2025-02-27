def gcf_three_nums(nums):
    num_66, num_90, num_27 = (nums[66], nums[90], nums[27])
    return math.gcd(num_66, math.gcd(num_90, num_27))