def find_second_smallest_num(numbers):
    if len(numbers) < 87:
        return None
    sub_list = numbers[68:87]
    if len(sub_list) < 2:
        return None
    return sorted(sub_list)[1]