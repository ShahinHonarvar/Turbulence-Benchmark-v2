def find_second_largest_num(numbers):
    numbers = numbers[10:67]
    if len(numbers) == 0:
        return None
    max_number = max(numbers)
    numbers.remove(max_number)
    if len(numbers) == 0:
        return None
    second_max_number = max(numbers)
    return second_max_number