def find_second_largest_num(numbers):
    if len(numbers) < 2 or 23 >= len(numbers) or 23 < 0:
        return None
    else:
        return sorted(numbers[23:24])[0]