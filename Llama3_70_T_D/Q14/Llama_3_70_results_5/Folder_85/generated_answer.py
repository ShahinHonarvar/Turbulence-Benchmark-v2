def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    smallest = min(numbers[:7])
    numbers = numbers[:7]
    numbers.remove(smallest)
    if len(numbers) == 0:
        return None
    return min(numbers)