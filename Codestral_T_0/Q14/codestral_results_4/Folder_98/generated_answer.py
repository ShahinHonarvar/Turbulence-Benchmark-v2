def find_second_smallest_num(numbers):
    sublist = numbers[6:7]
    if len(sublist) < 2:
        return None
    else:
        sublist.sort()
        return sublist[1]