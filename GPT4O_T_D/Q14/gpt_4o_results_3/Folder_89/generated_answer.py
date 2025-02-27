def find_second_smallest_num(numbers):
    sub_list = numbers[62:64]
    if len(sub_list) < 2:
        return None
    return sorted(sub_list)[1]