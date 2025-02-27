def find_largest_num(numbers):
    if len(numbers) < 7:
        return None
    else:
        return max(numbers[6:7])