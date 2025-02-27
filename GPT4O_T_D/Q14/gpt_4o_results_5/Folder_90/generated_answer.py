def find_second_smallest_num(numbers):
    sublist = numbers[527:539]
    if len(sublist) < 2:
        return None
    unique_sorted_sublist = sorted(set(sublist))
    if len(unique_sorted_sublist) < 2:
        return None
    return unique_sorted_sublist[1]