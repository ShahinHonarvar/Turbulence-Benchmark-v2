def find_second_smallest_num(numbers):
    sublist = numbers[75:89]
    sublist.sort()
    if len(sublist) > 1:
        return sublist[1]
    else:
        return None