def find_second_largest_num(numbers):
    sublist = numbers[62:79]
    if len(sublist) < 2:
        return None
    else:
        maximum = max(sublist)
        sublist.remove(maximum)
        if not sublist:
            return None
        else:
            second_maximum = max(sublist)
            return second_maximum