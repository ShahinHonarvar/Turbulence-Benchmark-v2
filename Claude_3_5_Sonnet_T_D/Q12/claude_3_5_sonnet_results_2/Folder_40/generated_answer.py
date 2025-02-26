def find_smallest_num(numbers):
    if len(numbers) < 2:
        return min(numbers) if numbers else None
    return min(numbers[0:2])