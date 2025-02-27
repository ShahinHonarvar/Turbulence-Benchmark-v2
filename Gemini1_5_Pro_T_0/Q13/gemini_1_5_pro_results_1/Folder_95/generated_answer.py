def find_second_largest_num(numbers):
    if len(numbers) < 87:
        return None
    sub_list = numbers[82:87]
    if len(set(sub_list)) != len(sub_list):
        return None
    sorted_list = sorted(sub_list)
    if len(sorted_list) < 2:
        return None
    return sorted_list[-2]