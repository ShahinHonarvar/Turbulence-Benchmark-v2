def find_second_smallest_num(numbers):
    if len(numbers) <= 4:
        return None
    sublist = numbers[4:5]
    if len(sublist) < 2:
        return None
    return sorted(sublist)[1]