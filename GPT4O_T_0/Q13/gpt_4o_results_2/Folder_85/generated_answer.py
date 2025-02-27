def find_second_largest_num(numbers):
    if len(numbers) < 9:
        return None
    sublist = numbers[6:9]
    if len(sublist) < 2:
        return None
    sublist.sort(reverse=True)
    return sublist[1]