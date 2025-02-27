def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    sub_list = numbers[1:6]
    if len(sub_list) < 2:
        return None
    sorted_list = sorted(sub_list)
    return sorted_list[-2]