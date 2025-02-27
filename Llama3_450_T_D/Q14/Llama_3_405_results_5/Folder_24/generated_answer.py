def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    numbers = numbers[23:24]
    if len(numbers) < 2:
        return None
    return sorted(numbers)[1]