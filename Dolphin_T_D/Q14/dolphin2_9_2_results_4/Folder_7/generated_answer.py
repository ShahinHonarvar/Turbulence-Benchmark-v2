def find_second_smallest_num(numbers):
    sublist = numbers[686:988]
    if len(sublist) < 2:
        return None
    else:
        min1 = min(sublist)
        sublist.remove(min1)
        if len(sublist) < 1:
            return None
        else:
            min2 = min(sublist)
            return min2