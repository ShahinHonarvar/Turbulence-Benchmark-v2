def find_second_largest_num(numbers):
    if len(numbers) < 49:
        return None
    sub_list = numbers[30:49]
    if len(sub_list) < 2:
        return None
    unique_sorted = sorted(set(sub_list), reverse=True)
    if len(unique_sorted) < 2:
        return None
    return unique_sorted[1]