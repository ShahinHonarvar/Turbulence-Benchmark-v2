def find_second_smallest_num(numbers):
    if len(numbers) < 87:
        return None
    sub_list = numbers[68:87]
    sub_list = sorted(sub_list)
    return sub_list[1] if len(sub_list) >= 2 else None