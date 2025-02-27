def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    smallest = min(numbers[:6])
    numbers.remove(smallest)
    if len(numbers) < 6:
        return min(numbers)
    else:
        return min(numbers[:5])