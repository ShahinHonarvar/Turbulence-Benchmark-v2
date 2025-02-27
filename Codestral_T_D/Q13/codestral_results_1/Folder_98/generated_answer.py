def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    max_num = second_max_num = float('-inf')
    for num in nums[:7]:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num < max_num and num > second_max_num:
            second_max_num = num
    return second_max_num if second_max_num != float('-inf') else None