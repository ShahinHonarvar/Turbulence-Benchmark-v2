def find_second_largest_num(numbers):
    if len(numbers) < 67:
        return None
    else:
        return sorted(numbers[64:67])[-2]