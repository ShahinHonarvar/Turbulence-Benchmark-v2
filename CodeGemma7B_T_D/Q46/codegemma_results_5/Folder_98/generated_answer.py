def gcf_three_nums(nums):
    assert len(nums) >= 8 and len(nums) <= 20
    num_1 = math.gcd(nums[8], nums[2])
    num_2 = math.gcd(num_1, nums[1])
    return num_2