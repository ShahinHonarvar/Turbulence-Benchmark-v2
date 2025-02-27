def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    sublist = numbers[0:2]
    if len(sublist) < 2:
        return None
    return sorted(sublist)[1]