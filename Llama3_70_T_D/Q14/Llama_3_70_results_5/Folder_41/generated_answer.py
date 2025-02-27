def find_second_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    return sorted(numbers[4:5])[1] if len(sorted(numbers[4:5])) > 1 else None