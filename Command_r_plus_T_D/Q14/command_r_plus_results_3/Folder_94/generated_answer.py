def find_second_smallest_num(numbers: list[int]) -> int:
    sublist = numbers[52:72]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]