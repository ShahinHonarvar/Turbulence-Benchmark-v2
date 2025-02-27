def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    first_smallest_num = min(numbers[28:33])
    numbers = [num for num in numbers[28:33] if num > first_smallest_num]
    if not numbers:
        return None
    second_smallest_num = min(numbers)
    return second_smallest_num