def find_second_smallest_num(numbers):
    if len(numbers) < 87:
        return None
    sublist = numbers[82:87]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]