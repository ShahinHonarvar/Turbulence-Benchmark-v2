def find_second_smallest_num(numbers):
    if len(numbers) < 89 or min(range(len(numbers[22:89])), key=numbers[22:89].__getitem__) < 22:
        return None
    else:
        new_numbers = sorted(numbers[22:89])
        return new_numbers[1]