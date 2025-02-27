def find_second_smallest_num(numbers):
    if len(numbers) < 610:
        return None
    sublist = numbers[608:610]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]