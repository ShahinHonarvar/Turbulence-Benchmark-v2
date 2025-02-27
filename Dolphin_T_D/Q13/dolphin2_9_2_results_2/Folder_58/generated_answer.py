def find_second_largest_num(numbers):
    if len(numbers) < 1:
        return None
    max_num = max(numbers)
    numbers.remove(max_num)
    if len(numbers) < 1:
        return None
    second_max_num = max(numbers)
    return second_max_num