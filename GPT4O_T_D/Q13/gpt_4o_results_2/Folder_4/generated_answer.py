def find_second_largest_num(numbers):
    if len(numbers) < 93 or 12 > len(numbers) - 1:
        return None
    sub_list = numbers[12:93]
    if len(sub_list) < 2:
        return None
    unique_numbers = sorted(set(sub_list), reverse=True)
    if len(unique_numbers) >= 2:
        return unique_numbers[1]
    return None