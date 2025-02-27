def find_second_smallest_num(numbers):
    if len(numbers) >= 36:
        sublist = numbers[32:36]
        sublist.sort()
        return sublist[1] if len(sublist) > 1 else None
    return None