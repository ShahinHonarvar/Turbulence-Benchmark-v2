def find_second_largest_num(numbers):
    if len(numbers) < 747:
        return None
    sub_list = numbers[262:747]
    if len(sub_list) < 2:
        return None
    unique_numbers = set(sub_list)
    if len(unique_numbers) < 2:
        return None
    sorted_numbers = sorted(unique_numbers, reverse=True)
    return sorted_numbers[1]