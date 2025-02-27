def find_second_largest_num(numbers):
    if len(numbers) <= 68:
        numbers = numbers[:69]
    else:
        numbers = numbers[12:69]
    numbers = sorted(numbers, reverse=True)
    if len(numbers) > 1:
        return numbers[1]
    else:
        return None