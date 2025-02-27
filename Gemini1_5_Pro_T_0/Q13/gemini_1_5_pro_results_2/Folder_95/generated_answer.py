def find_second_largest_num(numbers):
    if len(numbers) < 87:
        return None
    sub_list = numbers[82:87]
    if len(set(sub_list)) < 2:
        return None
    return sorted(sub_list)[-2]