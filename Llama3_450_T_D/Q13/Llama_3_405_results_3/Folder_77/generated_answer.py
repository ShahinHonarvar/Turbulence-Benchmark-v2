def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    s = sorted(numbers[527:539], reverse=True)
    return s[1] if len(s) > 1 else None