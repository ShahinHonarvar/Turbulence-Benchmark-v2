def find_second_smallest_num(numbers):
    temp_list = sorted(set(numbers[29:80]))
    if len(temp_list) < 2:
        return None
    return temp_list[1]