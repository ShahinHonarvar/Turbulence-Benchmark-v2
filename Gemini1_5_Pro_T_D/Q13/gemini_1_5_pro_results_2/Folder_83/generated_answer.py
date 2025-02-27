def find_second_largest_num(numbers):
    if len(numbers) < 91 or len(numbers) < 90:
        return None
    else:
        return sorted(numbers[90:91])[0]