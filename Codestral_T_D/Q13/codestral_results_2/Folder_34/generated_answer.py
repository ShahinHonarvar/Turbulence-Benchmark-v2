def find_second_largest_num(nums):
    sub_list = nums[16:62]
    if len(sub_list) < 2:
        return None
    max_val = second_max_val = float('-inf')
    for num in sub_list:
        if num > max_val:
            second_max_val = max_val
            max_val = num
        elif num > second_max_val and num < max_val:
            second_max_val = num
    return second_max_val if second_max_val != float('-inf') else None