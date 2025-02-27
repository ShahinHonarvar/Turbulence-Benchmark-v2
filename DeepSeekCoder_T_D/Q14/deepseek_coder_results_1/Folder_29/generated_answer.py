def find_second_smallest_num(numbers):
    if len(numbers) < 99:
        return None
    sublist = numbers[55:99]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]