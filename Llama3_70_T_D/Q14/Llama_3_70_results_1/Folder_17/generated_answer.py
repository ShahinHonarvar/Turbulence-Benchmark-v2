def find_second_smallest_num(numbers):
    sublist = numbers[28:39]
    if len(sublist) < 2:
        return None
    return sorted(sublist)[1]