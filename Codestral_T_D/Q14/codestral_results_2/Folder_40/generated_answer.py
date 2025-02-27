def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    smallest = min(numbers[:3])
    numbers.remove(smallest)
    if numbers:
        second_smallest = min(numbers[:3])
        return second_smallest
    return None