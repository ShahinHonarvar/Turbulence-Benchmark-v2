def find_second_smallest_num(numbers):
    if len(numbers) < 94:
        return None
    sublist = numbers[66:94]
    sublist.sort()
    if len(sublist) < 2:
        return None
    return sublist[1]