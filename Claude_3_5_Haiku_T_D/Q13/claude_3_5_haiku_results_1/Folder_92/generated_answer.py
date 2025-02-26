def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    largest = max(numbers[0], numbers[1])
    second_largest = min(numbers[0], numbers[1])
    return second_largest