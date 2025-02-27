def find_second_largest_num(numbers):
    if len(numbers) < 33:
        return None
    sub_list = numbers[28:33]
    unique_numbers = set(sub_list)
    if len(unique_numbers) < 2:
        return None
    unique_sorted = sorted(unique_numbers, reverse=True)
    return unique_sorted[1]