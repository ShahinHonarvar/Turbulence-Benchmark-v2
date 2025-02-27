def find_second_smallest_num(numbers):
    sublist = numbers[64:67]
    if len(sublist) >= 2:
        sublist.sort()
        return sublist[1]
    return None