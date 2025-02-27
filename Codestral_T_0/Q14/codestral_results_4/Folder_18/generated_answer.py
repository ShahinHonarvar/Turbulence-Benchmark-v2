def find_second_smallest_num(numbers):
    if 30 <= len(numbers) <= 48:
        sublist = sorted(numbers[30:49])
        if len(sublist) > 1:
            return sublist[1]
    return None