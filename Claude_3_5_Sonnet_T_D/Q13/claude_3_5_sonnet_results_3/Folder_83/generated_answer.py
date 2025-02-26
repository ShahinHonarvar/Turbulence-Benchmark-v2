def find_second_largest_num(numbers):
    if len(numbers) < 91 or len(set(numbers[90:91])) < 2:
        return None
    return sorted(set(numbers[90:91]))[-2]