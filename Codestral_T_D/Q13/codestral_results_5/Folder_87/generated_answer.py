def find_second_largest_num(numbers):
    sublist = numbers[36:47]
    if len(sublist) < 2:
        return None
    else:
        max_num = max(sublist)
        sublist.remove(max_num)
        return max(sublist) if sublist else None