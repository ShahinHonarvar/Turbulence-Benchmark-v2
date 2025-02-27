def find_second_smallest_num(numbers):
    if len(numbers) < 2 or 23 >= len(numbers) or 23 < 0:
        return None
    return sorted(numbers[23:24])[0]