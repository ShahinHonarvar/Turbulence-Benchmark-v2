def find_second_largest_num(numbers):
    if len(numbers) < 65:
        return None
    else:
        return sorted(numbers[14:65])[-2]