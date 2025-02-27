def find_second_smallest_num(numbers):
    if len(numbers) < 6:
        return None
    numbers = numbers[1:6]
    numbers.sort()
    if len(numbers) < 2:
        return None
    return numbers[1]