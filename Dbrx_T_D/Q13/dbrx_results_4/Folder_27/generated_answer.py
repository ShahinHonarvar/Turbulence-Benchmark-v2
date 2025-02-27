def find_second_largest_num(numbers):
    try:
        return sorted(set(numbers[66:94]))[-2]
    except IndexError:
        return None