def find_second_smallest_num(numbers):
    sublist = numbers[74:86]
    if len(sublist) < 2:
        return None
    smallest = min(sublist)
    sublist.remove(smallest)
    if len(sublist) > 1:
        second_smallest = min(sublist)
        return second_smallest
    else:
        return None