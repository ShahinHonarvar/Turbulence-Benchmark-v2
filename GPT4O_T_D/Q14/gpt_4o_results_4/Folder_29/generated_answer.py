def find_second_smallest_num(numbers):
    if len(numbers) < 99:
        return None
    sub_list = numbers[55:99]
    if len(set(sub_list)) < 2:
        return None
    return sorted(sub_list)[1]