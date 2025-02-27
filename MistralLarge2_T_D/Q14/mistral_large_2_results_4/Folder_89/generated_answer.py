def find_second_smallest_num(numbers):
    if len(numbers) < 64:
        return None
    sublist = sorted(numbers[62:64])
    if len(sublist) < 2:
        return None
    return sublist[1]