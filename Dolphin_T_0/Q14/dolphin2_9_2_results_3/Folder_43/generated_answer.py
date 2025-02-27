def find_second_smallest_num(numbers):
    if len(numbers) > 95:
        sublist = numbers[74:96]
        if len(set(sublist)) > 1:
            sublist.sort()
            return sublist[1]
    return None