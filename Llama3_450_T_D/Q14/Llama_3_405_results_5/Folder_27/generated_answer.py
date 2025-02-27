def find_second_smallest_num(numbers):
    sliced_list = numbers[25:60]
    if len(sliced_list) < 2:
        return None
    else:
        return sorted(sliced_list)[1]