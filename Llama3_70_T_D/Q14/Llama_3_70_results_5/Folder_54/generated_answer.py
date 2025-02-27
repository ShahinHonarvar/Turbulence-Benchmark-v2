def find_second_smallest_num(numbers):
    if len(numbers) < 87:
        return None
    sublist = sorted(set(numbers[68:87]))
    if len(sublist) < 2:
        return None
    return sublist[1]