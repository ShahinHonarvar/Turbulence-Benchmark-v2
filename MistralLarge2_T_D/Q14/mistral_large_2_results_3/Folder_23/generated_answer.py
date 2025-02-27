def find_second_smallest_num(numbers):
    if len(numbers) <= 92:
        return None
    sublist = numbers[19:93]
    if len(sublist) < 2:
        return None
    return sorted(sublist)[1]