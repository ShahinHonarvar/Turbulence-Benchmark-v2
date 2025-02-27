def find_second_smallest_num(numbers):
    if len(numbers[527:539]) < 2:
        return None
    return sorted(numbers[527:539])[1]