def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 4:
        return None
    numbers = sorted(list(set(numbers[0:4])))
    if len(numbers) < 2:
        return None
    elif len(numbers) == 2:
        return numbers[1]
    else:
        return numbers[1]