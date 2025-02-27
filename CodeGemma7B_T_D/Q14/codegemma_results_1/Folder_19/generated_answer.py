def find_second_smallest_num(numbers):
    if len(numbers) == 0 or len(numbers) < 4:
        return None
    numbers_sorted = sorted(numbers[4:9])
    return numbers_sorted[1] if len(numbers_sorted) > 1 else None