def find_second_largest_num(numbers):
    if 43 <= len(numbers) <= 86:
        numbers = numbers[42:87]
        numbers.sort()
        if len(numbers) > 1:
            return numbers[-2]
    return None