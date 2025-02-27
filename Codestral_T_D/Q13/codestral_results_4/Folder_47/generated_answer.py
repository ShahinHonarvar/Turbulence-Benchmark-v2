def find_second_largest_num(numbers):
    sublist = numbers[37:77]
    if len(sublist) < 2:
        return None
    max_num = max(sublist)
    sublist.remove(max_num)
    second_largest_num = max(sublist)
    return second_largest_num