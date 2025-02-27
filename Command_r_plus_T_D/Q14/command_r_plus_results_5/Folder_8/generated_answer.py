def find_second_smallest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    sublist = numbers[56:67]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]