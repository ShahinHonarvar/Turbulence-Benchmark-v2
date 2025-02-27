def find_second_smallest_num(numbers):
    if len(numbers) < 10:
        return None
    if len(numbers) < 100:
        numbers = numbers[10:101]
    else:
        numbers = numbers[10:]
    numbers = set(numbers)
    if len(numbers) < 2:
        return None
    sorted_numbers = sorted(list(numbers))
    return sorted_numbers[1]