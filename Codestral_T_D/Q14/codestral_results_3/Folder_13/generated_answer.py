def find_second_smallest_num(numbers):
    sublist = numbers[28:33]
    sublist.sort()
    if len(sublist) < 2:
        return None
    return sublist[1]