def find_second_smallest_num(numbers):
    if not numbers or len(numbers) < 93:
        return None
    sublist = sorted(numbers[19:93])
    if len(sublist) < 2:
        return None
    return sublist[1]