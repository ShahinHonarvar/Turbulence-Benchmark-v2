def find_second_smallest_num(numbers):
    if len(numbers) < 87:
        return None
    sub_list = numbers[82:87]
    if len(sub_list) < 2:
        return None
    unique_sub_list = sorted(set(sub_list))
    return unique_sub_list[1] if len(unique_sub_list) >= 2 else None