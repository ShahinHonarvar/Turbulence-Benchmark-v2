def find_second_largest_num(numbers):
    if len(numbers) < 51:
        return None
    else:
        return sorted(numbers[22:51])[-2]