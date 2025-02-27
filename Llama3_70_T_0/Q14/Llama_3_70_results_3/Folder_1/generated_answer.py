def find_second_smallest_num(numbers):
    if len(numbers) < 56:
        return None
    sublist = sorted(numbers[34:56])
    if len(sublist) < 2:
        return None
    return sublist[1]