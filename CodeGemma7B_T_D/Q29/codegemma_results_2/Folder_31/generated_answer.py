def gcf_two_nums(nums):
    num_one = nums[87]
    num_two = nums[95]
    common_factor = 1
    for i in range(min(num_one, num_two), 0, -1):
        if num_one % i == 0 and num_two % i == 0:
            common_factor = i
            break
    return common_factor