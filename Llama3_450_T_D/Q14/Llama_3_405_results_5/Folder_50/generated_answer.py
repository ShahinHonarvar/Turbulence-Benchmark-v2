def find_second_smallest_num(numbers):
    if len(numbers) < 69:
        return None
    sublist = numbers[42:69]
    if len(sublist) < 2:
        return None
    return sorted(sublist)[1]