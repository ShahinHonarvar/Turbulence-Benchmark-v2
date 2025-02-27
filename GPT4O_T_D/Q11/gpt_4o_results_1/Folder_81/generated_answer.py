def find_largest_num(numbers):
    if len(numbers) >= 101:
        return max(numbers[10:101])
    return None