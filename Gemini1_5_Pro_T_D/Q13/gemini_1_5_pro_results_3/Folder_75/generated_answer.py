def find_second_largest_num(numbers):
    if len(numbers) < 58:
        return None
    sublist = numbers[56:58]
    if len(sublist) == 1:
        return None
    else:
        sublist.sort()
        return sublist[0]