def find_second_largest_num(numbers):
    if len(numbers[1:9]) < 2:
        return None
    return sorted(set(numbers[1:9]))[-2]