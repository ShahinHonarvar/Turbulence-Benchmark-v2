def find_second_largest_num(numbers):
    numbers = numbers[75:95]
    if not numbers:
        return None
    max_num = max(numbers)
    numbers.remove(max_num)
    if not numbers:
        return None
    second_max_num = max(numbers)
    return second_max_num