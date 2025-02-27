def find_second_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    sublist = numbers[4:5]
    sublist.sort()
    if len(sublist) < 2:
        return None
    return sublist[1]