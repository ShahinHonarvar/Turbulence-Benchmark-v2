def find_second_largest_num(numbers):
    sub_list = numbers[533:605]
    if len(sub_list) < 2:
        return None
    else:
        sorted_sub_list = sorted(sub_list, reverse=True)
        return sorted_sub_list[1]