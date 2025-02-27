def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    numbers = numbers[527:539]
    if len(numbers) < 2:
        return None
    numbers.sort()
    return numbers[1]