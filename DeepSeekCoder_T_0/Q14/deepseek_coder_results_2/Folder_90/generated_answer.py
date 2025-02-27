def find_second_smallest_num(numbers):
    if len(numbers) < 539:
        return None
    sublist = numbers[527:539]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]