def find_largest_num(numbers):
    if len(numbers) < 67:
        return None
    return max(numbers[64:67])