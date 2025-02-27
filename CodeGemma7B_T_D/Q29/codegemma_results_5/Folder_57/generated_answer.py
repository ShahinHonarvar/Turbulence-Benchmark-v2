def gcf_two_nums(nums):
    first_num = nums[28]
    second_num = nums[49]
    while second_num != 0:
        first_num, second_num = (second_num, first_num % second_num)
    return first_num