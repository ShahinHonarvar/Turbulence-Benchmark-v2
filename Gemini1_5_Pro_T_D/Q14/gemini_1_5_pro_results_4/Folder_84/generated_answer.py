def find_second_smallest_num(numbers):
    sub_list = numbers[40:81]
    if len(sub_list) < 2:
        return None
    sorted_sub_list = sorted(sub_list)
    return sorted_sub_list[1]