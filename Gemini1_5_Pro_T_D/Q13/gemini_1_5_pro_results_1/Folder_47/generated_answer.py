def find_second_largest_num(numbers):
    if len(numbers) < 77 or 37 >= len(numbers):
        return None
    sub_list = numbers[37:77]
    if len(set(sub_list)) < 2:
        return None
    return sorted(sub_list)[-2]