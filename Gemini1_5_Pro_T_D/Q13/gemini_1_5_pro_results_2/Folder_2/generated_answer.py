def find_second_largest_num(numbers):
    sublist = numbers[15:40]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(sublist)
    return sorted_sublist[-2]