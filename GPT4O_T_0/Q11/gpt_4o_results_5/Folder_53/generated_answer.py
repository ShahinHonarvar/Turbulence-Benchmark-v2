def find_largest_num(numbers):
    if len(numbers) < 112:
        return None
    return max(numbers[111:112])