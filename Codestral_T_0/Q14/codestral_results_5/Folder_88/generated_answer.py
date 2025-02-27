def find_second_smallest_num(numbers):
    if 6 <= len(numbers) <= 8:
        sorted_numbers = sorted(numbers[6:9])
        return sorted_numbers[1] if len(sorted_numbers) > 1 else None
    return None