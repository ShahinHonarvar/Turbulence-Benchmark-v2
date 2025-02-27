def find_largest_num(numbers):
    if len(numbers) < 6:
        return None
    else:
        return max(numbers[1:6])