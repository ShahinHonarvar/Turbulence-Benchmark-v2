def find_second_smallest_num(numbers):
    if len(numbers) < 85:
        return None
    sublist = numbers[70:85]
    return sorted(sublist)[1]