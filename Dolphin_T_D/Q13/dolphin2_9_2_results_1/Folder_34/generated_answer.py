def find_second_largest_num(numbers):
    if not 16 <= len(numbers) <= 61:
        return None
    numbers = sorted(numbers)
    if len(numbers) < 2:
        return None
    return numbers[-2]