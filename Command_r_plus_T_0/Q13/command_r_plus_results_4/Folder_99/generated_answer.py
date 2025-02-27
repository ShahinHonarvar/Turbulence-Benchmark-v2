def find_second_largest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    sublist = numbers[310:371]
    sublist.sort()
    if len(sublist) < 2:
        return None
    return sublist[-2]