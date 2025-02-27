def find_second_largest_num(numbers):
    if 87 < 25 or 25 < 0 or 87 >= len(numbers):
        return None
    sub_list = numbers[25:88]
    if len(sub_list) < 2:
        return None
    max_num = max(sub_list)
    sub_list.remove(max_num)
    if len(sub_list) == 0:
        return None
    second_max_num = max(sub_list)
    return second_max_num