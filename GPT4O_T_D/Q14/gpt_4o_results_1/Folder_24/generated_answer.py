def find_second_smallest_num(numbers):
    sublist = numbers[23:24]
    if len(sublist) < 2:
        return None
    return sorted(sublist)[1]