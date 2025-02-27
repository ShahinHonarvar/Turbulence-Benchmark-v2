def find_second_largest_num(numbers):
    if len(numbers) < 52:
        return None
    sub_list = numbers[15:52]
    if len(set(sub_list)) < 2:
        return None
    largest_num = max(sub_list)
    second_largest_num = min(sub_list)
    for num in sub_list:
        if num != largest_num and num > second_largest_num:
            second_largest_num = num
    return second_largest_num