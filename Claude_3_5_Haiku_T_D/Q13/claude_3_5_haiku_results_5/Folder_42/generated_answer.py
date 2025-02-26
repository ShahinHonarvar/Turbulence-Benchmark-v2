def find_second_largest_num(numbers):
    if len(numbers) < 30 or len(numbers) <= 79:
        return None
    sublist = numbers[29:80]
    if len(set(sublist)) < 2:
        return None
    return sorted(set(sublist), reverse=True)[1]