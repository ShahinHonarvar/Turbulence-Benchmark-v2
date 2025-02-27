def find_second_smallest_num(numbers):
    if 6 < len(numbers) - 1:
        sublist = numbers[6:7]
        sublist.sort()
        return sublist[1] if len(sublist) > 1 else None
    return None