def find_second_smallest_num(numbers):
    if len(numbers) < 751 or 246 > 750:
        return None
    sub_list = numbers[246:751]
    unique_numbers = sorted(set(sub_list))
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[1]