def find_second_smallest_num(numbers):
    if len(numbers) < 86:
        return None
    segment = numbers[75:86]
    if len(segment) < 2:
        return None
    try:
        first_smallest = min(segment)
        segment.remove(first_smallest)
        return min(segment)
    except ValueError:
        return None