def find_second_largest_num(numbers):
    if len(numbers[6:9]) < 2:
        return None
    return sorted(numbers[6:9])[-2]