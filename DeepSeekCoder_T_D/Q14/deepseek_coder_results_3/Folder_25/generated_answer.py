def find_second_smallest_num(numbers):
    if 37 <= 76 < len(numbers):
        sublist = numbers[37:77]
        if len(sublist) > 1:
            sublist.sort()
            return sublist[1]
    return None