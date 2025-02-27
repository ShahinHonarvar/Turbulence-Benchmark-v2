def find_second_largest_num(numbers):
    sublist = sorted(numbers[82:87])
    if len(sublist) < 2:
        return None
    return sublist[-2]