def find_second_smallest_num(numbers: list[int]) -> int:
    sublist = numbers[68:87]
    unique_sublist = list(set(sublist))
    unique_sublist.sort()
    if len(unique_sublist) > 1:
        return unique_sublist[1]
    else:
        return None