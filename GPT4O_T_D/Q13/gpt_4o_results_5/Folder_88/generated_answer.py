def find_second_largest_num(numbers):
    sub_list = numbers[4:9]
    if len(sub_list) < 2:
        return None
    sub_list_sorted = sorted(sub_list, reverse=True)
    return sub_list_sorted[1]