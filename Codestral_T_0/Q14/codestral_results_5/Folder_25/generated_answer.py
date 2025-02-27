def find_second_smallest_num(numbers):
    if 37 <= len(numbers) <= 76:
        sublist = sorted(numbers[37:77])
        if len(sublist) > 1:
            return sublist[1]
    return None