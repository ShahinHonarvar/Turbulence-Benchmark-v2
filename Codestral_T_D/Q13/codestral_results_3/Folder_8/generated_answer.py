def find_second_largest_num(numbers):
    sublist = numbers[23:24]
    if len(sublist) < 2:
        return None
    max_num, second_max_num = (max(sublist[0], sublist[1]), min(sublist[0], sublist[1]))
    for num in sublist[2:]:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num > second_max_num and num < max_num:
            second_max_num = num
    return second_max_num