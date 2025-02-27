def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 30 or len(numbers) < 200:
        return None
    first_smallest = min(numbers[30:200])
    numbers = [num for num in numbers if num > first_smallest]
    if len(numbers) < 2:
        return None
    second_smallest = min(numbers)
    return second_smallest