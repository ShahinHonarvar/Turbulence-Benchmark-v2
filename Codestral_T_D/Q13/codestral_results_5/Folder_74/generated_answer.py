def find_second_largest_num(numbers):
    sub_list = sorted(numbers[17:79])
    if len(sub_list) >= 2:
        return sub_list[-2]
    else:
        return None