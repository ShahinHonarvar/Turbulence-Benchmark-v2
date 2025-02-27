def find_smallest_num(numbers):
    if len(numbers) < 9:
        return None
    return min(numbers[4:9])