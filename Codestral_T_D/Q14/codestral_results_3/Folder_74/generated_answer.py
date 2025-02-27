def find_second_smallest_num(numbers):
    sublist = sorted(numbers[36:47])
    if len(sublist) < 2:
        return None
    return sublist[1]