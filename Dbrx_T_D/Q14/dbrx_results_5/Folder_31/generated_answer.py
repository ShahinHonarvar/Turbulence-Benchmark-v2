def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 94:
        return None
    min_num = min(numbers[29:94])
    numbers = [num for num in numbers[29:94] if num > min_num]
    second_min_num = min(numbers) if len(numbers) > 1 else None
    return second_min_num