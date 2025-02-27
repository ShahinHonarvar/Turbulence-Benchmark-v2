def find_second_largest_num(numbers):
    if len(numbers) < 24:
        return None
    else:
        return sorted(numbers[23:24])[1] if len(set(numbers[23:24])) > 1 else None