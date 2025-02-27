def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    max_num = nums[686]
    second_max_num = None
    for i in range(687, 988):
        if nums[i] > max_num:
            second_max_num = max_num
            max_num = nums[i]
        elif nums[i] > second_max_num:
            second_max_num = nums[i]
    return second_max_num