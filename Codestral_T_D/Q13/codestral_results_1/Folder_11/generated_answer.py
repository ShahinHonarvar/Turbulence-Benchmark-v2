def find_second_largest_num(numbers):
    sub_list = numbers[37:52]
    if len(sub_list) < 2:
        return None
    else:
        sub_list.sort()
        return sub_list[-2]