def find_largest_num(numbers):
    if len(numbers) < 98:
        return None
    return max(numbers[21:98])