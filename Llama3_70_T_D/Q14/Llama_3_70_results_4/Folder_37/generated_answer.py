def find_second_smallest_num(numbers):
    temp_list = sorted(numbers[5:8])
    if len(temp_list) < 2:
        return None
    else:
        return temp_list[1]