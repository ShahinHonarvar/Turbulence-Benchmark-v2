def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    first_smallest = min(numbers[:2])
    second_smallest = max(numbers[:2])
    return second_smallest if second_smallest != first_smallest else None