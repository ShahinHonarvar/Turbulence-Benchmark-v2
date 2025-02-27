def find_smallest_num(numbers):
    if len(numbers) < 610:
        return None
    return min(numbers[608:610])