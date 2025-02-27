def find_largest_num(numbers):
    if len(numbers) < 7:
        return None
    return max(numbers[0:7])