def find_second_largest_num(numbers):
    sublist = numbers[22:89]
    if len(sublist) >= 2:
        return sorted(sublist)[-2]
    else:
        return None