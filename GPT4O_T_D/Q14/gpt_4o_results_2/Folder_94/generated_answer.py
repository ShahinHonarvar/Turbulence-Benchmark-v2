def find_second_smallest_num(numbers):
    if len(numbers) < 72:
        return None
    sub_list = numbers[52:72]
    if len(sub_list) < 2:
        return None
    unique_numbers = set(sub_list)
    if len(unique_numbers) < 2:
        return None
    sorted_unique_numbers = sorted(unique_numbers)
    return sorted_unique_numbers[1]