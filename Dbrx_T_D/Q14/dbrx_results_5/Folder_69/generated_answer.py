def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 25:
        return None
    first_smallest = min(numbers[25:88])
    numbers = [num for num in numbers[25:88] if num > first_smallest]
    if not numbers:
        return None
    second_smallest = min(numbers)
    return second_smallest