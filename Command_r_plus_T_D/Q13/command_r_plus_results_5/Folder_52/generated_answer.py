def find_second_largest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    sublist = numbers[28:39]
    sublist.sort()
    if len(sublist) < 2:
        return None
    else:
        return sublist[-2]