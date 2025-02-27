def find_second_largest_num(numbers):
    sublist = numbers[22:89]
    if len(sublist) < 2:
        return None
    else:
        sublist.sort(reverse=True)
        return sublist[1]