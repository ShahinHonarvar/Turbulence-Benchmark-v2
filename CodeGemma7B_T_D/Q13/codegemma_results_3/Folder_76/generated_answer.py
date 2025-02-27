def find_second_largest_num(nums):
    if len(nums) < 987 - 686 + 1:
        return None
    max_num = float('-inf')
    second_max_num = float('-inf')
    for i in range(686, 988):
        if nums[i] > max_num:
            second_max_num = max_num
            max_num = nums[i]
        elif nums[i] > second_max_num and nums[i] != max_num:
            second_max_num = nums[i]
    return second_max_num