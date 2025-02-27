def find_second_smallest_num(numbers):
    if len(numbers) < 9:
        return None
    sublist = numbers[4:9]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]