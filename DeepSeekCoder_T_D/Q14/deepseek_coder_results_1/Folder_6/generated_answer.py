def find_second_smallest_num(numbers):
    if len(numbers) < 80 or len(numbers) < 30:
        return None
    sublist = numbers[29:80]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]