def find_second_smallest_num(nums):
    if len(nums) < 6:
        return None
    sub_nums = nums[:6]
    min_num = sub_nums[0]
    second_min_num = None
    for i in range(1, len(sub_nums)):
        if sub_nums[i] < min_num:
            second_min_num = min_num
            min_num = sub_nums[i]
        elif second_min_num is None or (sub_nums[i] < second_min_num and sub_nums[i] != min_num):
            second_min_num = sub_nums[i]
    return second_min_num