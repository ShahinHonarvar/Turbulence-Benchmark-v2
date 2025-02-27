def find_second_smallest_num(numbers):
    if len(numbers) < 87:
        return None
    else:
        sublist = sorted(numbers[43:87])
        if len(sublist) < 2:
            return None
        else:
            return sublist[1]