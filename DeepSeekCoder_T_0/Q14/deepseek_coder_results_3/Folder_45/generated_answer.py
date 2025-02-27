def find_second_smallest_num(numbers):
    if len(numbers) < 201 or numbers[30:201].count(min(numbers[30:201])) >= 2:
        return None
    return sorted(set(numbers[30:201]))[1] if len(set(numbers[30:201])) > 1 else None