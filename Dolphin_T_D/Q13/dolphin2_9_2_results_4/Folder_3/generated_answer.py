def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    numbers = numbers[62:93]
    max_num = max(numbers)
    numbers.remove(max_num)
    if len(numbers) < 2:
        return None
    second_max_num = max(numbers)
    return second_max_num