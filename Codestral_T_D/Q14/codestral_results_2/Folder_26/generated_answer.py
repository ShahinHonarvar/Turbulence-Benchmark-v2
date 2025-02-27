def find_second_smallest_num(numbers):
    sublist = sorted(numbers[62:79])
    return sublist[1] if len(sublist) > 1 else None