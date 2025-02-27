def find_second_largest_num(numbers):
    numbers = list(set(numbers[246:751]))
    numbers.sort()
    if len(numbers) < 2:
        return None
    else:
        return numbers[-2]