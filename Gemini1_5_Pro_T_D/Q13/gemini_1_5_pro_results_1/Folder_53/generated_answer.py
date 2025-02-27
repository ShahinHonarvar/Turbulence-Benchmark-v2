def find_second_largest_num(numbers):
    sub_list = numbers[100:201]
    if len(sub_list) < 2:
        return None
    else:
        sorted_sub_list = sorted(sub_list)
        return sorted_sub_list[-2]