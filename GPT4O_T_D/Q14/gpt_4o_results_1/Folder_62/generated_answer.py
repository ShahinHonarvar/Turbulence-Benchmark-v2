def find_second_smallest_num(numbers):
    sub_list = numbers[10:67]
    if len(sub_list) < 2:
        return None
    sub_list_sorted = sorted(sub_list)
    return sub_list_sorted[1]