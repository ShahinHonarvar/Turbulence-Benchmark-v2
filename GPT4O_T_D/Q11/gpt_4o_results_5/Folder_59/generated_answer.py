def find_largest_num(numbers):
    if len(numbers) > 9:
        return max(numbers[9:10])
    return None