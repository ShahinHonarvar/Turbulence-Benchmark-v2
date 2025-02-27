def find_second_smallest_num(numbers: list[int]) -> int:
    sublist = numbers[28:39]
    sublist.sort()
    if len(sublist) < 2:
        return None
    return sublist[1]