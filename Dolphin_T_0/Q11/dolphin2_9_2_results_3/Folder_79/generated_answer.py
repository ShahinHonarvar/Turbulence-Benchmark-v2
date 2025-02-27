def find_largest_num(numbers):
    sublist = numbers[4:5]
    if len(sublist) == 0:
        return None
    else:
        return max(sublist)