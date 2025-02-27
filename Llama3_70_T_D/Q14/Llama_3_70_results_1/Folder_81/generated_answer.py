def find_second_smallest_num(numbers):
    if len(numbers) <= 100:
        return None
    return sorted(set(numbers[10:101]))[1]