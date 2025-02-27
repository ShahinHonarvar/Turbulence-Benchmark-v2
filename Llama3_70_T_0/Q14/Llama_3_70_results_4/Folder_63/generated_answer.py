def find_second_smallest_num(numbers):
    if len(numbers) < 83:
        return None
    sublist = numbers[56:83]
    sublist.sort()
    if len(sublist) < 2:
        return None
    return sublist[1]