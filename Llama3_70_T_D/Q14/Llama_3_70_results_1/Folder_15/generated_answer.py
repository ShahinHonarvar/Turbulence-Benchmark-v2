def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    smallest = min(numbers[:4])
    numbers.remove(smallest)
    if numbers:
        second_smallest = min(numbers[:4])
        return second_smallest
    else:
        return None