def find_second_largest_num(nums):
    if len(nums) == 0 or len(nums) < 98:
        return None
    sublist = nums[21:97]
    if len(sublist) < 2:
        return None
    max_num = sublist[0]
    second_max_num = None
    for num in sublist:
        if num > max_num:
            second_max_num, max_num = (max_num, num)
        elif num < max_num and num > second_max_num:
            second_max_num = num
    return second_max_num