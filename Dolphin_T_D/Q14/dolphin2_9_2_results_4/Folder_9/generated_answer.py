def find_second_smallest_num(numbers):
    if len(numbers) < 200:
        return None
    sublist = numbers[70:201]
    if len(sublist) < 2:
        return None
    sublist.sort()
    if sublist[1] == sublist[0]:
        return None
    return sublist[1]