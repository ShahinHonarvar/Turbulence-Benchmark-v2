def find_second_largest_num(numbers):
    sub_list = sorted(numbers[68:87])
    if len(sub_list) < 2:
        return None
    return sub_list[-2]