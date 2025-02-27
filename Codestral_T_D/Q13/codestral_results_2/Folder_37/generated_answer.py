def find_second_largest_num(numbers):
    sublist = numbers[1:6]
    sorted_sublist = sorted(sublist)
    if len(sorted_sublist) < 2:
        return None
    else:
        return sorted_sublist[-2]