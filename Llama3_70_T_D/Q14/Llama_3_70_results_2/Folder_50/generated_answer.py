def find_second_smallest_num(numbers):
    numbers = numbers[42:69]
    if len(numbers) < 2:
        return None
    else:
        return sorted(numbers)[1]