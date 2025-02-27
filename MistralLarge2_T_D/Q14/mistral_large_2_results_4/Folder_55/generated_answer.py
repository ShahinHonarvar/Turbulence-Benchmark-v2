def find_second_smallest_num(numbers):
    if len(numbers) > 10:
        sublist = sorted(numbers[10:11])
        if len(sublist) > 1:
            return sublist[1]
    return None