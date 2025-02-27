def find_second_largest_num(nums):
    if len(nums[62:100]) < 2:
        return None
    max_num = second_max = float('-inf')
    for num in nums[62:100]:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif num > second_max and num < max_num:
            second_max = num
    return second_max