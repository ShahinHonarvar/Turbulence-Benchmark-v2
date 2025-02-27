def find_second_largest_num(numbers):
    if len(numbers) < 91:
        return None
    else:
        return sorted(numbers[90:91])[1] if len(set(numbers[90:91])) > 1 else None