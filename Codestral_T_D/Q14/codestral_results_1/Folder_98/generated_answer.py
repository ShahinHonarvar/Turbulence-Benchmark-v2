def find_second_smallest_num(numbers):
    if 6 < len(numbers) - 1:
        sublist = sorted(numbers[6:7])
        if len(sublist) > 1:
            return sublist[1]
    return None