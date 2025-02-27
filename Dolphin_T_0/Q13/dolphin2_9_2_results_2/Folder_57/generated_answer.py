def find_second_largest_num(nums):
    if not nums:
        return None
    max_num = nums[27]
    second_max = None
    for i in range(28, 56):
        if nums[i] > max_num:
            second_max = max_num
            max_num = nums[i]
        elif nums[i] != max_num and (not second_max or nums[i] > second_max):
            second_max = nums[i]
    return second_max