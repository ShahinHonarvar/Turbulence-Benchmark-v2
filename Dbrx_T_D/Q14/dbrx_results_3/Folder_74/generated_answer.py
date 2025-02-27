def find_second_smallest_num(numbers):
    numbers = numbers[36:47]
    if len(numbers) < 2:
        return None
    elif len(numbers) == 2:
        return min(numbers)
    else:
        first_smallest = min(numbers)
        numbers = [num for num in numbers if num > first_smallest]
        second_smallest = min(numbers)
        return second_smallest