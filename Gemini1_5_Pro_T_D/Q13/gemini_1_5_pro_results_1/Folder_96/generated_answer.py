def find_second_largest_num(numbers):
    if len(numbers) < 52 or 15 > len(numbers):
        return None
    sub_list = numbers[15:52]
    if len(set(sub_list)) < 2:
        return None
    largest_num = max(sub_list)
    second_largest_num = min(sub_list)
    for i in range(15, 52):
        if numbers[i] != largest_num and numbers[i] > second_largest_num:
            second_largest_num = numbers[i]
    return second_largest_num