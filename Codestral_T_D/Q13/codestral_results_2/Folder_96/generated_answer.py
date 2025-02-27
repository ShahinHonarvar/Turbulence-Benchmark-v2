def find_second_largest_num(numbers):
    sublist = sorted(numbers[15:52], reverse=True)
    if len(sublist) < 2:
        return None
    return sublist[1]