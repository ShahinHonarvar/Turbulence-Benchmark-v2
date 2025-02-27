def find_second_smallest_num(numbers):
    sublist = numbers[20:31]
    if len(sublist) < 2:
        return None
    return sorted(sublist)[1]