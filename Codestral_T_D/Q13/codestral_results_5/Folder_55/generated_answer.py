def find_second_largest_num(numbers):
    if len(numbers) <= 1:
        return None
    else:
        numbers = numbers[0:11]
        numbers.sort()
        return numbers[-2] if len(numbers) > 1 else None