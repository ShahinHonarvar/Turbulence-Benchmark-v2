def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    max_num = second_max_num = float('-inf')
    for i in range(200, 201):
        if i < len(nums):
            num = nums[i]
            if num > max_num:
                second_max_num = max_num
                max_num = num
            elif num > second_max_num and num != max_num:
                second_max_num = num
    if second_max_num == float('-inf'):
        return None
    return second_max_num