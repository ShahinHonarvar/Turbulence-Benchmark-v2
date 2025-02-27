def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    smallest = min(numbers[:7])
    numbers[:7].remove(smallest)
    if not numbers[:7]:
        return None
    return min(numbers[:7])