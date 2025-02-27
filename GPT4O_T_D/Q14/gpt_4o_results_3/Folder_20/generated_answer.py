def find_second_smallest_num(numbers):
    if len(numbers) < 95 or len(numbers[75:95]) < 2:
        return None
    sublist = numbers[75:95]
    sublist.sort()
    return sublist[1] if len(sublist) > 1 else None