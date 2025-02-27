def find_second_largest_num(numbers):
    sub_list = numbers[310:371]
    if len(sub_list) < 2:
        return None
    else:
        sorted_list = sorted(sub_list)
        return sorted_list[-2]