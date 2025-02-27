def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    smallest = min(numbers[:7])
    numbers = [num for num in numbers[:7] if num != smallest]
    if len(numbers) == 0:
        return None
    return min(numbers)