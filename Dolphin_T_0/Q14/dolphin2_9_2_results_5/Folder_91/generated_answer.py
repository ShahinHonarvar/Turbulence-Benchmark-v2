def find_second_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    smallest = min(numbers[:6])
    numbers.remove(smallest)
    if len(numbers) < 5:
        return None
    return min(numbers[:6])