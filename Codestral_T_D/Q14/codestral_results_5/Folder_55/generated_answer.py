def find_second_smallest_num(numbers):
    if 10 < len(numbers) - 1:
        sublist = numbers[10:11]
        sublist.sort()
        return sublist[1] if len(sublist) > 1 else None
    else:
        return None