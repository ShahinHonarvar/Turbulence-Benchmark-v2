def find_second_smallest_num(numbers):
    sublist = numbers[75:86]
    if len(sublist) < 2:
        return None
    else:
        sorted_sublist = sorted(sublist)
        return sorted_sublist[1]