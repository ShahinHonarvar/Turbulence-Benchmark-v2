def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    return min(numbers[0], numbers[1])