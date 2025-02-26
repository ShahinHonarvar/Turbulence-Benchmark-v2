def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    smallest = min(numbers[0], numbers[0])
    second_smallest = max(numbers[0], numbers[0])
    if smallest == second_smallest:
        return None
    return second_smallest