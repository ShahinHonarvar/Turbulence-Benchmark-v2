def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    numbers = numbers[91:100]
    min_num = min(numbers)
    numbers.remove(min_num)
    if not numbers:
        return None
    second_min_num = min(numbers)
    return second_min_num