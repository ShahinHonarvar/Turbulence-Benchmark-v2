def find_second_smallest_num(numbers):
    if len(numbers) < 11:
        return None
    sub_list = numbers[10:101]
    if len(sub_list) < 2:
        return None
    unique_numbers = sorted(set(sub_list))
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[1]