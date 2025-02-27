def find_largest_num(numbers):
    if not numbers or len(numbers) < 100:
        return None
    return max(numbers[91:100])