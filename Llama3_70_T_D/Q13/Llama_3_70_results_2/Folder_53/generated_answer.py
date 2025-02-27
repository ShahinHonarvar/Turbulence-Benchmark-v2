def find_second_largest_num(numbers):
    if len(numbers) < 201:
        return None
    return sorted(set(numbers[100:201]), reverse=True)[1] if len(set(numbers[100:201])) > 1 else None