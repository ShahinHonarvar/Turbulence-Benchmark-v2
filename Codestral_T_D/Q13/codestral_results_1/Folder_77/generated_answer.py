def find_second_largest_num(numbers):
    sublist = numbers[527:538]
    if len(sublist) < 2:
        return None
    else:
        sorted_sublist = sorted(sublist, reverse=True)
        return sorted_sublist[1]