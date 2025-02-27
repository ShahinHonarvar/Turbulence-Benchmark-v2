def find_second_largest_num(numbers):
    if len(numbers) < 58:
        return None
    sublist = numbers[56:58]
    if len(set(sublist)) == 1:
        return None
    return sorted(sublist)[0]