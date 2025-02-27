def find_second_largest_num(numbers):
    if len(numbers) < 69:
        return None
    sublist = numbers[42:69]
    sublist.sort(reverse=True)
    if len(sublist) < 2:
        return None
    return sublist[1]