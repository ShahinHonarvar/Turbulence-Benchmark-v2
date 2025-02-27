def find_smallest_num(numbers):
    if len(numbers) < 81:
        return None
    return min(numbers[80:81])