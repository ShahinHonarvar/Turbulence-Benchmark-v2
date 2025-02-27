def find_second_largest_num(numbers):
    if len(numbers) < 88:
        return None
    sublist = numbers[25:88]
    sublist.sort(reverse=True)
    if len(sublist) < 2:
        return None
    return sublist[1]