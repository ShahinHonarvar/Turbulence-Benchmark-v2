def find_second_smallest_num(numbers):
    if 28 <= len(numbers) <= 32:
        sublist = sorted(numbers[28:33])
        if len(sublist) > 1:
            return sublist[1]
    return None