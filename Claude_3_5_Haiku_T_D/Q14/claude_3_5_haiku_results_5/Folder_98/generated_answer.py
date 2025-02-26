def find_second_smallest_num(numbers):
    if len(numbers) <= 6:
        return None
    sublist = numbers[6:7]
    if not sublist:
        return None
    return sublist[0]