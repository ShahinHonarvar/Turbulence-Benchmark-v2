def find_second_smallest_num(numbers):
    if len(numbers) < 78:
        return None
    sublist = numbers[66:78]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]