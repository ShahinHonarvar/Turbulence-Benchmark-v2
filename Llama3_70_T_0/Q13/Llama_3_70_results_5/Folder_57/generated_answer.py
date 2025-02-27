def find_second_largest_num(numbers):
    if len(numbers) < 56:
        return None
    else:
        return sorted(numbers[27:56])[-2]