def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    max_num = max(numbers)
    numbers.remove(max_num)
    second_max = max(numbers)
    return second_max