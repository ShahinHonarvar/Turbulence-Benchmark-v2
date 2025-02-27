def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    first, second = (1, 0) if numbers[0] > numbers[1] else (0, 1)
    return numbers[second]