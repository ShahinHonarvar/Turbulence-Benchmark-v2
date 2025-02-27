def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    max_num = max(numbers[19:93])
    if max_num == max(numbers):
        return None
    return max_num