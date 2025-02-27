def find_second_largest_num(numbers):
    if len(numbers) < 7:
        return None
    else:
        return sorted(numbers[6:7])[1] if len(set(numbers[6:7])) > 1 else None