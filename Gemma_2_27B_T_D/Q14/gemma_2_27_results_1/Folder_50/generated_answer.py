def find_second_smallest_num(numbers):
    if len(numbers[42:69]) < 2:
        return None
    return sorted(numbers[42:69])[1]