def find_second_largest_num(numbers):
    sub_list = numbers[10:67]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    else:
        return sub_list[-2]