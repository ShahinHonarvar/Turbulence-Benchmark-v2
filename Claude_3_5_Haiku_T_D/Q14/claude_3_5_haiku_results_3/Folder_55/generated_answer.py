def find_second_smallest_num(numbers):
    if len(numbers) < 11:
        return None
    sublist = numbers[10:11]
    if not sublist:
        return None
    return sublist[0]