def find_second_largest_num(numbers):
    sublist = numbers[17:79]
    sublist.sort(reverse=True)
    if len(sublist) < 2:
        return None
    else:
        return sublist[1]