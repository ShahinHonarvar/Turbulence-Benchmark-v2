def find_second_smallest_num(numbers):
    if len(numbers) < 201:
        return None
    numbers = numbers[30:201]
    numbers.sort()
    if len(numbers) < 2:
        return None
    return numbers[1]