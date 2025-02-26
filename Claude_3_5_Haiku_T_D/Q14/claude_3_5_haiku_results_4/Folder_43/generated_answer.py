def find_second_smallest_num(numbers):
    if len(numbers) < 96:
        return None
    segment = numbers[74:96]
    if len(segment) < 2:
        return None
    sorted_segment = sorted(segment)
    return sorted_segment[1]