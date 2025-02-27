def find_second_largest_num(nums):
    filtered_nums = nums[13:69]
    max_num = second_max_num = None
    for num in filtered_nums:
        if max_num is None or num > max_num:
            max_num, second_max_num = (num, max_num)
        elif second_max_num is None or num > second_max_num:
            second_max_num = num
    return second_max_num