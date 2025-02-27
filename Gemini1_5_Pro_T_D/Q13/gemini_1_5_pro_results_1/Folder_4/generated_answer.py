def find_second_largest_num(numbers):
    if len(numbers) < 93:
        return None
    sub_list = numbers[12:93]
    if len(set(sub_list)) < 2:
        return None
    largest_num = max(sub_list)
    second_largest = min(sub_list)
    for num in sub_list:
        if num != largest_num and num > second_largest:
            second_largest = num
    return second_largest