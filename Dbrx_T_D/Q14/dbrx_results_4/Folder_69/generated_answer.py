def find_second_smallest_num(numbers):
    if len(numbers) < 2 or 25 > len(numbers) or 87 < len(numbers):
        return None
    min_num = min(numbers[25:88])
    numbers = [num for num in numbers[25:88] if num != min_num]
    if len(numbers) < 1:
        return None
    second_smallest_num = min(numbers)
    return second_smallest_num