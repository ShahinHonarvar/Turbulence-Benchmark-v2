def gcf_three_nums(nums):
    num_one = nums[4]
    num_two = nums[0]
    num_three = nums[8]
    gcf_one_two = math.gcd(num_one, num_two)
    gcf_three_two = math.gcd(num_three, gcf_one_two)
    return gcf_three_two