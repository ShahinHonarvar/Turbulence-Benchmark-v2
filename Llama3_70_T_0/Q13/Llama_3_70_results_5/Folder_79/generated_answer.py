def find_second_largest_num(numbers):
    if len(numbers) < 5:
        return None
    else:
        return sorted(numbers[4:5])[1] if len(set(numbers[4:5])) > 1 else None