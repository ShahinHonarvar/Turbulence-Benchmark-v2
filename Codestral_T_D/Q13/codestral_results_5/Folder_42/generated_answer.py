def find_second_largest_num(numbers):
    sublist = numbers[29:80]
    if len(sublist) < 2:
        return None
    else:
        first_largest = max(sublist)
        sublist.remove(first_largest)
        return max(sublist) if sublist else None