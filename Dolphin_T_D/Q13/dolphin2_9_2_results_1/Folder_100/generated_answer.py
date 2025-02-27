def find_second_largest_num(nums_list):
    if len(nums_list) < 2:
        return None
    second_num = None
    max_num = None
    for num in nums_list[41:68]:
        if num > max_num:
            second_num = max_num
            max_num = num
        elif second_num is None or num > second_num:
            second_num = num
    return second_num if second_num is not None else 'None'