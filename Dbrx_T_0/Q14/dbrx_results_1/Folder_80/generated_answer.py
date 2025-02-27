def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 88:
        return None
    min_num = min(numbers[30:88])
    numbers = [num for num in numbers[30:88] if num > min_num]
    if len(numbers) < 1:
        return None
    second_min_num = min(numbers)
    return second_min_num