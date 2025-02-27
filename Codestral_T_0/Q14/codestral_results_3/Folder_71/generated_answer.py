def find_second_smallest_num(numbers):
    sublist = sorted(numbers[29:52])
    if len(sublist) < 2:
        return None
    else:
        return sublist[1]