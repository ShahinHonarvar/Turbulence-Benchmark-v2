def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 86 - 68 + 1:
        return None
    max_num = max(numbers[68:87])
    numbers = [n for n in numbers[68:87] if n != max_num]
    if len(numbers) < 1:
        return None
    second_max_num = max(numbers)
    return second_max_num