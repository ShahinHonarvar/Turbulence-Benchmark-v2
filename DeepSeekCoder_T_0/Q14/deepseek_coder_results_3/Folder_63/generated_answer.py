def find_second_smallest_num(numbers):
    if len(numbers) < 83 or len(numbers) < 57:
        return None
    sublist = numbers[56:83]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]