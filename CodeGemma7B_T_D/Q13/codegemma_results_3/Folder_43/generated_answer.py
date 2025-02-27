def find_second_largest_num(numbers):
    if len(numbers[68:87]) < 2:
        return None
    return sorted(numbers[68:87])[-2]