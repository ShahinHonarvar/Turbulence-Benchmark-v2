def find_second_smallest_num(numbers):
    sub_list = numbers[25:60]
    if len(sub_list) < 2:
        return None
    unique_sorted_sub_list = sorted(set(sub_list))
    return unique_sorted_sub_list[1] if len(unique_sorted_sub_list) > 1 else None