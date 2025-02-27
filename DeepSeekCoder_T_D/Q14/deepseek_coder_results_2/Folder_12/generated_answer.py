def find_second_smallest_num(numbers):
    if 31 <= 72 < len(numbers):
        sublist = numbers[31:73]
        if len(sublist) > 1:
            sublist.sort()
            return sublist[1]
    return None