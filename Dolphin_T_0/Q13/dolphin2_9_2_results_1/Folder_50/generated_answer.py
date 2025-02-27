def find_second_largest_num(numbers):
    sublist = numbers[70:85]
    if len(sublist) < 2:
        return None
    max_num = max(sublist)
    sublist.remove(max_num)
    if len(sublist) >= 2:
        second_max_num = max(sublist)
        return second_max_num
    else:
        return None