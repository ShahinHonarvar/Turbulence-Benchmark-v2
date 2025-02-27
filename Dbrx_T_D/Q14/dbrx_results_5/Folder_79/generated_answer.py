def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers[1:6]) < 2:
        return None
    first_smallest = min(numbers[1:6])
    numbers = [num for num in numbers[1:6] if num > first_smallest]
    if not numbers:
        return None
    return min(numbers)