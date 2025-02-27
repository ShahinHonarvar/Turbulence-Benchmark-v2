def find_second_smallest_num(numbers):
    if len(numbers) < 49:
        return None
    sublist = sorted(numbers[30:49])
    if len(sublist) < 2:
        return None
    return sublist[1]