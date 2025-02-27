def find_second_smallest_num(numbers):
    sublist = numbers[22:51]
    if len(sublist) < 2:
        return None
    min_num = min(sublist)
    sublist.remove(min_num)
    return min(sublist)