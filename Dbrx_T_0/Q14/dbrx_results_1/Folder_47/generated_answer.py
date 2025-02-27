def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 63 - 22 + 1:
        return None
    min_num = min(numbers[22:63])
    numbers = [num for num in numbers[22:63] if num > min_num]
    if not numbers:
        return None
    second_min_num = min(numbers)
    return second_min_num