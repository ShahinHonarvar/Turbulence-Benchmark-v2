def find_second_largest_num(numbers):
    sublist = numbers[62:79]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(sublist, reverse=True)
    return sorted_sublist[1]