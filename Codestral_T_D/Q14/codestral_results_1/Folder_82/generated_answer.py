def find_second_smallest_num(numbers):
    sublist = sorted(numbers[20:201])
    if len(sublist) > 1:
        return sublist[1]
    return None