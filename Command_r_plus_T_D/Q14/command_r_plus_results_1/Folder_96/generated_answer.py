def find_second_smallest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    sublist = numbers[50:201]
    unique_sublist = list(set(sublist))
    if len(unique_sublist) < 2:
        return None
    unique_sublist.sort()
    return unique_sublist[1]