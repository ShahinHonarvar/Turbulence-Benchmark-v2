def find_largest_num(numbers):
    if len(numbers) < 371:
        return None
    return max(numbers[310:371])