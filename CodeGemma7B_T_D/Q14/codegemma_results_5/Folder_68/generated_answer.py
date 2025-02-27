def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    if len(numbers) > 8:
        numbers = numbers[:9]
    numbers.sort()
    return numbers[1]