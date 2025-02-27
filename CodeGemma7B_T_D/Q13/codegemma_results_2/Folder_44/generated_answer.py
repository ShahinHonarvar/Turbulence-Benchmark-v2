def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    numbers.sort()
    return numbers[-2] if len(numbers) > 13 and len(numbers) > 68 else None