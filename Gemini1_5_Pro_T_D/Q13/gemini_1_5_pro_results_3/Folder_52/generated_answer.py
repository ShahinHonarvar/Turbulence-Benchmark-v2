def find_second_largest_num(numbers):
    sub_list = numbers[28:39]
    if len(sub_list) < 2:
        return None
    else:
        return sorted(sub_list)[-2]