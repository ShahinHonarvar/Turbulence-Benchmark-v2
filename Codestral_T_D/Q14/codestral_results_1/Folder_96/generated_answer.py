def find_second_smallest_num(numbers):
    sublist = sorted(numbers[50:201])
    if len(sublist) >= 2:
        return sublist[1]
    else:
        return None