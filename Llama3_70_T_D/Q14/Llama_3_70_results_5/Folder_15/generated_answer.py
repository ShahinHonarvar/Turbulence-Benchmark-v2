def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    smallest = min(numbers[:4])
    numbers.remove(smallest)
    return min(numbers[:4]) if numbers else None