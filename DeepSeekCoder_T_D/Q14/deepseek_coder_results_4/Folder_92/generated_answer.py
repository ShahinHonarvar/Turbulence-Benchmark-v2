def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    first_two = sorted(numbers[:2])
    return first_two[1] if len(first_two) > 1 else None