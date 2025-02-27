def find_second_smallest_num(numbers):
    if len(numbers) < 201:
        return None
    numbers = numbers[50:201]
    numbers.sort()
    if len(numbers) == 1:
        return None
    return numbers[1]