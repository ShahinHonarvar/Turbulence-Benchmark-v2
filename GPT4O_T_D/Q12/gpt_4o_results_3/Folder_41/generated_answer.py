def find_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    return min(numbers[4:5])