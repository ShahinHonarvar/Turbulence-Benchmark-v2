def find_second_largest_num(numbers):
    sub_list = numbers[686:988]
    if len(sub_list) < 2:
        return None
    else:
        return sorted(sub_list)[-2]