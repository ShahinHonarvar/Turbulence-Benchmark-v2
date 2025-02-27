def find_second_smallest_num(numbers):
    sublist = numbers[527:539]
    sorted_sublist = sorted(sublist)
    if len(sorted_sublist) >= 2:
        return sorted_sublist[1]
    return None