def find_second_largest_num(numbers):
    sublist = sorted(numbers[25:88])
    if len(sublist) < 2:
        return None
    else:
        return sublist[-2]