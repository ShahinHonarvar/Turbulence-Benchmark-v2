def find_second_largest_num(numbers):
    if len(numbers) < 39:
        return None
    segment = numbers[28:39]
    if len(segment) < 2:
        return None
    segment.sort()
    return segment[-2]