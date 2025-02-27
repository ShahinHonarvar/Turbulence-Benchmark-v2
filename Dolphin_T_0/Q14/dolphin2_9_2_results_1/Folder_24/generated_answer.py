def find_second_smallest_num(numbers):
    if 23 <= len(numbers) < 24:
        return None
    else:
        sublist = numbers[23:24]
        sublist.sort()
        if len(sublist) >= 2:
            return sublist[1]
        else:
            return None