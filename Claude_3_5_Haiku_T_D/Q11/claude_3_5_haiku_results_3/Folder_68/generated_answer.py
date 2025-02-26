def find_largest_num(numbers):
    if len(numbers) < 9:
        return max(numbers)
    return max(numbers[0:9])