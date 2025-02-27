def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    max_num = max(numbers)
    numbers_without_max = [num for num in numbers if num != max_num]
    if len(numbers_without_max) < 2:
        return None
    second_max_num = max(numbers_without_max)
    return second_max_num