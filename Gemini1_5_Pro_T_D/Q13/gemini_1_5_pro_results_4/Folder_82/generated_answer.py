def find_second_largest_num(numbers):
    if len(numbers) < 203:
        return None
    sub_list = numbers[20:201]
    sorted_list = sorted(sub_list)
    if len(sorted_list) < 2:
        return None
    return sorted_list[-2]