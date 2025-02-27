def find_second_largest_num(numbers):
    if len(numbers) < 40:
        return None
    else:
        return sorted(numbers[15:40])[-2]