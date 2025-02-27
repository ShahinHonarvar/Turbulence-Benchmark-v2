def find_second_largest_num(numbers):
    if len(numbers) < 30:
        return None
    sub_list = numbers[30:201]
    if len(sub_list) < 2:
        return None
    sorted_list = sorted(sub_list)
    return sorted_list[-2]