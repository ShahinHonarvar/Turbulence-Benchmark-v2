def find_second_largest_num(numbers):
    if len(numbers) < 52:
        return None
    else:
        return sorted(numbers[29:52])[-2]