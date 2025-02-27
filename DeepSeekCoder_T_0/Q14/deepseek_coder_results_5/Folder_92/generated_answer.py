def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    first_smallest = min(numbers[0], numbers[1])
    second_smallest = max(numbers[0], numbers[1])
    return second_smallest