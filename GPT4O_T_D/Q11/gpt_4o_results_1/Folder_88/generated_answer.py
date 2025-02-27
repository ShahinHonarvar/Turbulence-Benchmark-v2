def find_largest_num(numbers):
    if len(numbers) < 9:
        return None
    return max(numbers[4:9])