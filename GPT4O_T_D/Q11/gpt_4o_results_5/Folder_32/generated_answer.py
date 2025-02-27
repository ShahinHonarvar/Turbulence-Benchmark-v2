def find_largest_num(numbers):
    if len(numbers) < 98 or not numbers:
        return None
    return max(numbers[21:98])