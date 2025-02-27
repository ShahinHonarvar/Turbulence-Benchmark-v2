def find_second_largest_num(numbers):
    if len(numbers) < 64:
        return None
    else:
        return sorted(numbers[22:64])[-2]