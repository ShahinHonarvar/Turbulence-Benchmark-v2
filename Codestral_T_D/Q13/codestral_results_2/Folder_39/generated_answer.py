def find_second_largest_num(numbers):
    sublist = sorted(numbers[20:31], reverse=True)
    if len(sublist) < 2:
        return None
    else:
        return sublist[1]