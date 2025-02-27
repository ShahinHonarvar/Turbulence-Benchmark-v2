def find_second_largest_num(numbers):
    if len(numbers) < 60:
        return None
    else:
        return sorted(numbers[25:60])[-2]