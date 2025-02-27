def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    limited_list = numbers[:8]
    unique_numbers = set(limited_list)
    if len(unique_numbers) < 2:
        return None
    sorted_numbers = sorted(unique_numbers, reverse=True)
    return sorted_numbers[1]