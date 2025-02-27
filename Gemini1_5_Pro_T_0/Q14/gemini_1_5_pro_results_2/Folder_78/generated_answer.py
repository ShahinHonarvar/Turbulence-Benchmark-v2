def find_second_smallest_num(numbers):
    if len(numbers) < 79 or 17 > len(numbers):
        return None
    sublist = numbers[17:79]
    if len(set(sublist)) < 2:
        return None
    return sorted(set(sublist))[1]