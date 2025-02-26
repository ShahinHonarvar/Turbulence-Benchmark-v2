def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    first_two = numbers[:2]
    smallest = min(first_two)
    second_smallest = max(first_two)
    if smallest == second_smallest:
        return None
    return second_smallest