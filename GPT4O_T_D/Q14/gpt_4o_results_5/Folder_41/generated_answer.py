def find_second_smallest_num(numbers):
    sublist = numbers[4:5]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1] if len(sublist) > 1 else None