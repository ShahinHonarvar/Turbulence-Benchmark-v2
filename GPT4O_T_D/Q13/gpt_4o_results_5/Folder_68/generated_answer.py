def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers[:9]) < 2:
        return None
    unique_numbers = set(numbers[:9])
    if len(unique_numbers) < 2:
        return None
    sorted_numbers = sorted(unique_numbers, reverse=True)
    return sorted_numbers[1]