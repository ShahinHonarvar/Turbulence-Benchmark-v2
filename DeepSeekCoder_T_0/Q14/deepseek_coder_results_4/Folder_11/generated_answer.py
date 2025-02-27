def find_second_smallest_num(numbers):
    if len(numbers) < 94:
        return None
    sublist = numbers[66:94]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]