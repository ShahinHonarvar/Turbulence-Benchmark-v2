def find_second_smallest_num(numbers):
    sublist = numbers[7:9]
    if len(sublist) == 0:
        return None
    elif len(sublist) == 1:
        return None
    else:
        sublist.sort()
        return sublist[1]