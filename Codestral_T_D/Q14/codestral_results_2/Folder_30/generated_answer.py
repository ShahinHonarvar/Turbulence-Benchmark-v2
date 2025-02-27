def find_second_smallest_num(numbers):
    sublist = numbers[26:53]
    if len(sublist) < 2:
        return None
    else:
        smallest = min(sublist)
        sublist.remove(smallest)
        return min(sublist)