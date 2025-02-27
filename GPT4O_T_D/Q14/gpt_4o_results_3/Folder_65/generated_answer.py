def find_second_smallest_num(numbers):
    if len(numbers) < 58:
        return None
    segment = numbers[56:58]
    if len(segment) < 2:
        return None
    return sorted(segment)[1]