def find_second_largest_num(numbers):
    if len(numbers) < 91:
        return None
    else:
        target_numbers = numbers[90:]
        return sorted(set(target_numbers), reverse=True)[1] if len(set(target_numbers)) > 1 else None