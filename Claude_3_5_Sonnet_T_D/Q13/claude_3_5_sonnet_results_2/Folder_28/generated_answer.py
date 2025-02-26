def find_second_largest_num(numbers):
    sublist = numbers[62:64]
    if len(sublist) < 2:
        return None
    return min(sublist)