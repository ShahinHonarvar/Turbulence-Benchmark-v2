def find_second_smallest_num(numbers):
    sublist = numbers[28:41]
    sublist.sort()
    if len(sublist) >= 2:
        return sublist[1]
    return None