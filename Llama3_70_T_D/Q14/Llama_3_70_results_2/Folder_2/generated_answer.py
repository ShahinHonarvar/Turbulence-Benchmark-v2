def find_second_smallest_num(numbers):
    if not numbers or len(numbers) < 87:
        return None
    sublist = sorted(numbers[43:87])
    if len(sublist) < 2 or sublist[0] == sublist[1]:
        return None
    return sublist[1]