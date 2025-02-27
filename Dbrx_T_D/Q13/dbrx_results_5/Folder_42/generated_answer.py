def find_second_largest_num(numbers):
    sub_list = numbers[29:80]
    if len(sub_list) < 2:
        return None
    first, second = (max(sub_list[0], sub_list[1]), min(sub_list[0], sub_list[1]))
    for num in sub_list[2:]:
        if num > first:
            first, second = (num, first)
        elif num > second and num != first:
            second = num
    return second