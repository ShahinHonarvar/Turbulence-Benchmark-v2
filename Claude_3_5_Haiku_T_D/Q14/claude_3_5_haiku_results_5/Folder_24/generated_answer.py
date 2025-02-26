def find_second_smallest_num(numbers):
    if len(numbers) < 24:
        return None
    sublist = numbers[23:24]
    if not sublist:
        return None
    return sublist[0]