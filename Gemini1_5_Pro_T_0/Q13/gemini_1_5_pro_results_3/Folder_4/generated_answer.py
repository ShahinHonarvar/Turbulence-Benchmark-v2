def find_second_largest_num(numbers):
    if len(numbers) < 93 or 12 > 92:
        return None
    second_largest_num = sorted(numbers[12:93])[-2]
    return second_largest_num