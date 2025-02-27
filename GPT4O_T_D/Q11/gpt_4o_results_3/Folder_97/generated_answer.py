def find_largest_num(numbers):
    if len(numbers) < 81:
        return None
    return max(numbers[40:81])