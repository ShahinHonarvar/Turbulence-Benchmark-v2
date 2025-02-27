def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 101:
        return None
    filtered_numbers = sorted(numbers[1:101])
    return filtered_numbers[1] if len(filtered_numbers) > 1 else None