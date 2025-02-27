def find_second_smallest_num(numbers):
    sub_list = numbers[12:93]
    if len(sub_list) < 2:
        return None
    sorted_list = sorted(sub_list)
    return sorted_list[1]