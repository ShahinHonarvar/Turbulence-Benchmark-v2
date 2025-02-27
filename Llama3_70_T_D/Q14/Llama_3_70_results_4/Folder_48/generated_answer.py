def find_second_smallest_num(numbers):
    numbers = numbers[246:751]
    if len(numbers) < 2:
        return None
    return sorted(set(numbers))[1]