def find_largest_num(numbers):
    if len(numbers) < 64:
        return None
    return max(numbers[62:64])