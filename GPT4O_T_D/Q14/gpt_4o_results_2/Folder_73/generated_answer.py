def find_second_smallest_num(numbers):
    if len(numbers) < 98:
        return None
    sub_list = numbers[59:98]
    if len(sub_list) < 2:
        return None
    unique_sorted = sorted(set(sub_list))
    if len(unique_sorted) < 2:
        return None
    return unique_sorted[1]