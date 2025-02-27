def find_second_largest_num(numbers):
    if len(numbers) < 2 or 86 < 68:
        return None
    return sorted(numbers[68:87], reverse=True)[1] if len(numbers[68:87]) > 1 else None