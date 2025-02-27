def find_second_smallest_num(numbers):
    if len(numbers) < 12:
        return None
    second_smallest_num = sorted(numbers[10:101])[1]
    return second_smallest_num