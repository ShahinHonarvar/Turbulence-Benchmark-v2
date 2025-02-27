def find_second_largest_num(numbers):
    if len(numbers) < 94:
        return None
    else:
        return sorted(numbers[29:94])[-2]