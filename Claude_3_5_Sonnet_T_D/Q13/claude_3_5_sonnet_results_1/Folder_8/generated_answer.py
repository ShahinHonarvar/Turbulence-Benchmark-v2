def find_second_largest_num(numbers):
    if len(numbers) <= 23 or len(numbers[23:24]) < 2:
        return None
    return sorted(numbers[23:24], reverse=True)[1] if len(numbers[23:24]) > 1 else None