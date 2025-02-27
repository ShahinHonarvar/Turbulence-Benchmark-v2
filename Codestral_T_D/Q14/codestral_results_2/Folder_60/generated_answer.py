def find_second_smallest_num(numbers):
    if len(numbers) <= 98:
        return None
    sublist = numbers[56:99]
    sublist.sort()
    if len(sublist) < 2:
        return None
    return sublist[1]