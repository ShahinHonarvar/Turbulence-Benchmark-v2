def find_second_smallest_num(numbers):
    if len(numbers) < 89:
        return None
    sub_list = numbers[22:89]
    if len(sub_list) < 2:
        return None
    unique_sorted_sublist = sorted(set(sub_list))
    if len(unique_sorted_sublist) < 2:
        return None
    return unique_sorted_sublist[1]