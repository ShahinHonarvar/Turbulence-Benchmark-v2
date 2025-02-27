def find_second_smallest_num(numbers):
    if len(numbers) > 85:
        sublist = numbers[75:86]
        sublist.sort()
        return sublist[1] if len(sublist) > 1 else None
    return None