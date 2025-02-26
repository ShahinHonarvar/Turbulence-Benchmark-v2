def find_largest_num(numbers):
    if len(numbers) < 2:
        return max(numbers) if numbers else None
    return max(numbers[0], numbers[1])