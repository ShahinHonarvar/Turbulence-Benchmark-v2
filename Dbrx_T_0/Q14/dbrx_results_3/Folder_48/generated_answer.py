def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 750 - 246 + 1:
        return None
    min_num = min(numbers[246:751])
    numbers = [num for num in numbers[246:751] if num > min_num]
    if not numbers:
        return None
    second_min_num = min(numbers)
    return second_min_num