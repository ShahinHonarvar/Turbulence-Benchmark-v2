def find_second_largest_num(numbers):
    if len(numbers) > 23:
        numbers = numbers[:24]
    if len(numbers) < 24:
        return None
    numbers = numbers[23:24]
    if len(numbers) == 0:
        return None
    if len(numbers) == 1:
        return None
    numbers.sort(reverse=True)
    return numbers[1]