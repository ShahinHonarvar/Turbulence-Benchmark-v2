def find_second_smallest_num(numbers):
    sub_list = sorted(numbers[60:201])
    if len(sub_list) < 2:
        return None
    return sub_list[1]