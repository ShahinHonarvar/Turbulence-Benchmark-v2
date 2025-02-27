def find_second_smallest_num(numbers):
    if len(numbers) < 87:
        return None
    sub_list = numbers[82:87]
    if len(sub_list) < 2:
        return None
    unique_sorted = sorted(sub_list)
    return unique_sorted[1] if len(unique_sorted) >= 2 else None