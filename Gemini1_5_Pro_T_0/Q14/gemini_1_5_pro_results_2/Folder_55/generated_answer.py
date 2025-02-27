def find_second_smallest_num(numbers):
    if len(numbers) < 11:
        return None
    return sorted(numbers[10:11])[0]