def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 7:
        return None
    unique_numbers = set(numbers[0:7])
    if len(unique_numbers) < 2:
        return None
    sorted_numbers = sorted(unique_numbers)
    return sorted_numbers[-2]