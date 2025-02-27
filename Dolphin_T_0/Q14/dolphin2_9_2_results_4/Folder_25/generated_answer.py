def find_second_smallest_num(numbers):
    if 76 < len(numbers) and 37 < len(numbers):
        sublist = numbers[37:77]
        sublist.sort()
        if len(sublist) > 1:
            return sublist[1]
    return None