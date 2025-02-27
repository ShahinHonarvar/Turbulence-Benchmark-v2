def find_second_smallest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    sublist = numbers[82:87]
    sublist.sort()
    if len(sublist) < 2:
        return None
    else:
        return sublist[1]