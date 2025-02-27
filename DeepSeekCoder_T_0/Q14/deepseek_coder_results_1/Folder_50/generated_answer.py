def find_second_smallest_num(numbers):
    if len(numbers) < 69 or len(numbers) < 43:
        return None
    sublist = numbers[42:69]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]