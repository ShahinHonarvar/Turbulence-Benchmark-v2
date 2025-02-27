def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    smallest = min(numbers[:6])
    numbers.remove(smallest)
    if len(numbers) < 1:
        return None
    second_smallest = min(numbers[:5])
    return second_smallest