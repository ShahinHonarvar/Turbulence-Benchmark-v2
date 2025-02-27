def find_second_largest_num(numbers):
    if len(numbers) < 55:
        return None
    segment = numbers[50:55]
    if len(set(segment)) < 2:
        return None
    return sorted(segment)[-2]