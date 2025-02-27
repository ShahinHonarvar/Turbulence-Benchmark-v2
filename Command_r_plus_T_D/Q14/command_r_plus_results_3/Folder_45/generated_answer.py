def find_second_smallest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    sublist = sorted(numbers[30:201])
    if len(sublist) < 2:
        return None
    else:
        return sublist[1]