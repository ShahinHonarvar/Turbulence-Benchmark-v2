def gcf_two_nums(nums):
    num_1 = nums[83]
    num_2 = nums[14]
    greatest_common_factor = None
    for i in range(1, min(num_1, num_2) + 1):
        if num_1 % i == 0 and num_2 % i == 0:
            greatest_common_factor = i
    return greatest_common_factor