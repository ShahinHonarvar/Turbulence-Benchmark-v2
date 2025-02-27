def find_second_smallest_num(numbers):
    if len(numbers) < 52:
        return None
    sublist = numbers[26:53]
    if len(set(sublist)) < 2:
        return None
    return sorted(sublist)[1]