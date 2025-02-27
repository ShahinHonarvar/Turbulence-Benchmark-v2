def find_second_largest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    sublist = numbers[52:72]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]