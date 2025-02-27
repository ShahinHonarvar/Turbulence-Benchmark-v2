def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    max_num = second_max_num = float('-inf')
    for num in nums[5:8]:
        if num > max_num:
            second_max_num, max_num = (max_num, num)
        elif second_max_num < num < max_num:
            second_max_num = num
    return second_max_num if second_max_num != float('-inf') else None