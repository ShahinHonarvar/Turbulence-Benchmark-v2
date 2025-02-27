def find_second_smallest_num(numbers):
    if len(numbers) != 5:
        return None
    sublist = numbers[3:6]
    if len(set(sublist)) == 1:
        return None
    sublist.sort()
    return sublist[1]