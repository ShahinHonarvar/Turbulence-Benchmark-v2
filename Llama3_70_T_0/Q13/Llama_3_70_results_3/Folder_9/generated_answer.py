def find_second_largest_num(numbers):
    if len(numbers) < 201:
        return None
    else:
        return sorted(numbers[200:201])[1] if len(set(numbers[200:201])) > 1 else None