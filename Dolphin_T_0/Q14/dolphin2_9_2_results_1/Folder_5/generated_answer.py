def find_second_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    sublist = numbers[3:6]
    sublist.sort()
    if len(set(sublist)) < 2:
        return None
    return sublist[1]