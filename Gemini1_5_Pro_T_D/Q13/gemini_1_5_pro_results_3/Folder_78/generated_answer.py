def find_second_largest_num(numbers):
    sublist = numbers[43:52]
    if len(sublist) < 2:
        return None
    else:
        sorted_sublist = sorted(sublist)
        return sorted_sublist[-2]