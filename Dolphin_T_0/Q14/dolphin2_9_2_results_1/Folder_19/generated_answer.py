def find_second_smallest_num(numbers):
    if 4 <= len(numbers) <= 8:
        return None
    sublist = numbers[4:9]
    sublist.sort()
    if len(sublist) < 2:
        return None
    return sublist[1]