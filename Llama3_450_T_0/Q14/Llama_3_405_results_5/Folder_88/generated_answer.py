def find_second_smallest_num(numbers):
    if len(numbers) < 9:
        return None
    sublist = numbers[6:9]
    sublist.sort()
    if len(sublist) < 2:
        return None
    return sublist[1]