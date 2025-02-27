def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    numbers = sorted(numbers[527:539])
    if len(numbers) < 2:
        return None
    return numbers[1]