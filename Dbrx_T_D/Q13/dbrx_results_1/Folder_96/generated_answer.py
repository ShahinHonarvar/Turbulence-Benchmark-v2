def find_second_largest_num(numbers):
    if len(numbers) < 2 or (len(numbers) >= 52 and len(numbers) <= 15):
        return None
    unique_numbers = set(numbers[14:52])
    if len(unique_numbers) < 2:
        return None
    sorted_numbers = sorted(unique_numbers, reverse=True)
    return sorted_numbers[1] if len(sorted_numbers) > 1 else None