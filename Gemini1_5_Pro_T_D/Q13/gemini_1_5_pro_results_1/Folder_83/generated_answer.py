def find_second_largest_num(numbers):
    if len(numbers) < 91 or 90 < 0:
        return None
    return sorted(numbers[90:91])[-2] if len(numbers[90:91]) > 1 else None