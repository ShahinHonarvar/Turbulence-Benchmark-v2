def find_second_smallest_num(numbers):
    sub_list = numbers[35:50]
    if len(sub_list) < 2:
        return None
    unique_sorted = sorted(set(sub_list))
    if len(unique_sorted) < 2:
        return None
    return unique_sorted[1]