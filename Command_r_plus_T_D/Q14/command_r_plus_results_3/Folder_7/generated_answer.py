def find_second_smallest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    sublist = numbers[686:988]
    unique_sublist = list(set(sublist))
    unique_sublist.sort()
    if len(unique_sublist) < 2:
        return None
    else:
        return unique_sublist[1]