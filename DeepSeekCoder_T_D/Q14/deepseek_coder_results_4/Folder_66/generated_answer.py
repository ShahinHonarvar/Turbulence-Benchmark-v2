def find_second_smallest_num(numbers):
    if len(numbers) < 100:
        return None
    sublist = numbers[62:100]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]