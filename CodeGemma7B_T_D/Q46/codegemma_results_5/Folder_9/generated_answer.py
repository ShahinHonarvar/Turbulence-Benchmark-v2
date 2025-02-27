def gcf_three_nums(nums):
    num_one = nums[66]
    num_two = nums[90]
    num_three = nums[27]
    common_factor = max(num_one, num_two, num_three)
    while True:
        if num_one % common_factor == 0 and num_two % common_factor == 0 and (num_three % common_factor == 0):
            return common_factor
        else:
            common_factor -= 1