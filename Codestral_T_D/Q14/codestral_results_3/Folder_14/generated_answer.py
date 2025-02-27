def find_second_smallest_num(numbers):
    sublist = numbers[8:10]
    if len(sublist) >= 2:
        sublist.sort()
        return sublist[1]
    else:
        return None