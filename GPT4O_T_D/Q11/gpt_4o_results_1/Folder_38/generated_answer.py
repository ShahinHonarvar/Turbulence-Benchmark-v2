def find_largest_num(numbers):
    if len(numbers) <= 63:
        return None
    return max(numbers[22:64])