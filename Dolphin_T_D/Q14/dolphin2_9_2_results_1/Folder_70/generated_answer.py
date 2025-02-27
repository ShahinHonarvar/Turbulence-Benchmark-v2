def find_second_smallest_num(numbers):
    sublist = numbers[35:50]
    if len(sublist) < 2:
        return None
    min_num = min(sublist)
    sublist.remove(min_num)
    second_min = min(sublist) if sublist else None
    return second_min