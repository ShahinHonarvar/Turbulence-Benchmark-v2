def find_second_largest_num(numbers):
    if len(numbers) <= 90:
        return None
    sublist = sorted(numbers[90:91])
    return sublist[-2] if len(sublist) >= 2 else None