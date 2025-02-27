def find_second_largest_num(numbers):
    if len(numbers) < 58:
        return None
    else:
        return sorted(numbers[56:58])[1]