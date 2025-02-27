def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    max_num = max(numbers)
    numbers.remove(max_num)
    if len(numbers) < 2:
        return None
    return max(numbers)