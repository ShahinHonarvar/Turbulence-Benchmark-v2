def find_second_largest_num(nums):
    sub_nums = nums[10:101]
    if len(sub_nums) < 2:
        return None
    max_num = max(sub_nums)
    second_max_num = None
    for num in sub_nums:
        if num != max_num and (second_max_num is None or num > second_max_num):
            second_max_num = num
    return second_max_num