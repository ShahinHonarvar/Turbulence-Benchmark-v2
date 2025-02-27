def find_second_smallest_num(numbers):
    if len(numbers) < 52:
        return None
    sub_list = numbers[29:52]
    unique_sorted = sorted(set(sub_list))
    if len(unique_sorted) < 2:
        return None
    return unique_sorted[1]