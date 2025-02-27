def find_second_largest_num(numbers):
    if len(numbers) < 93:
        return None
    else:
        return sorted(numbers[19:93])[-2]