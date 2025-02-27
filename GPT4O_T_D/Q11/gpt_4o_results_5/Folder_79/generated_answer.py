def find_largest_num(numbers):
    if len(numbers) <= 4:
        return None
    return max(numbers[4:5])