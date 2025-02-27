def find_second_smallest_num(numbers):
    if len(numbers) < 539 or 527 >= len(numbers):
        return None
    sublist = numbers[527:539]
    if len(set(sublist)) < 2:
        return None
    return sorted(set(sublist))[1]