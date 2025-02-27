def gcf_three_nums(nums):
    num_16 = nums[16]
    num_87 = nums[87]
    num_95 = nums[95]
    return math.gcd(num_16, math.gcd(num_87, num_95))