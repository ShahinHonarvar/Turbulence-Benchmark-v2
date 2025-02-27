def gcf_three_nums(nums):
    num_1 = nums[29]
    num_2 = nums[74]
    num_3 = nums[49]
    current_gcf = num_1
    if num_2 < current_gcf:
        current_gcf = num_2
    if num_3 < current_gcf:
        current_gcf = num_3
    while True:
        if current_gcf % num_1 == 0 and current_gcf % num_2 == 0 and (current_gcf % num_3 == 0):
            return current_gcf
        current_gcf -= 1