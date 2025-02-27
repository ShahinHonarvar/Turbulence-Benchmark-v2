def find_largest_num(numbers):
    if len(numbers) < 10:
        return None
    subset = numbers[8:10]
    return max(subset)