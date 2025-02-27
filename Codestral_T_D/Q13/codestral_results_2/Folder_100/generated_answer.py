def find_second_largest_num(numbers):
    segment = numbers[42:69]
    if len(segment) >= 2:
        segment.sort(reverse=True)
        return segment[1]
    return None