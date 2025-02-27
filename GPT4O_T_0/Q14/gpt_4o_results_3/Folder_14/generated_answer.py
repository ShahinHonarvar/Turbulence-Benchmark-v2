def find_second_smallest_num(numbers):
    if len(numbers) < 10:
        return None
    sublist = numbers[8:10]
    if len(sublist) < 2:
        return None
    return sorted(sublist)[1]