def find_second_smallest_num(numbers):
    if len(numbers) < 10:
        return None
    unique_numbers = sorted(numbers[:10])
    return unique_numbers[1] if len(unique_numbers) > 1 else None