def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 19 or len(numbers) > 92:
        return None
    first_smallest = min(numbers[18:93])
    numbers = [n for n in numbers[18:93] if n > first_smallest]
    second_smallest = None
    if numbers:
        second_smallest = min(numbers)
    return second_smallest