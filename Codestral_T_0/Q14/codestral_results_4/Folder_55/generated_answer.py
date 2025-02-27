def find_second_smallest_num(numbers):
    if 10 < len(numbers) - 1:
        sublist = sorted(numbers[10:11])
        if len(sublist) > 1:
            return sublist[1]
    return None