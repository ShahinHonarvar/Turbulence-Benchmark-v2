def find_second_smallest_num(numbers):
    if len(numbers) < 69:
        return None
    else:
        return sorted(numbers[13:69])[1]