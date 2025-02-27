def find_second_smallest_num(numbers):
    if 74 <= len(numbers) <= 95:
        sublist = sorted(numbers[74:96])
        if len(sublist) > 1:
            return sublist[1]
    return None