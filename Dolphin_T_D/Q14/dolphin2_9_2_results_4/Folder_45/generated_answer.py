def find_second_smallest_num(numbers):
    sublist = numbers[30:200]
    if len(sublist) < 2:
        return None
    smallest = min(sublist)
    sublist.remove(smallest)
    if not sublist:
        return None
    return min(sublist)