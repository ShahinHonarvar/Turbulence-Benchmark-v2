def find_second_smallest_num(numbers):
    if len(numbers) < 88:
        return None
    sub_list = numbers[25:88]
    if len(sub_list) < 2:
        return None
    unique_sorted_sub_list = sorted(set(sub_list))
    if len(unique_sorted_sub_list) < 2:
        return None
    return unique_sorted_sub_list[1]