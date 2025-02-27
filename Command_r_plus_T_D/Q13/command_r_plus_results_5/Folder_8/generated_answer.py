def find_second_largest_num(numbers: list[int]) -> int:
    if len(numbers) < 24:
        return None
    else:
        sublist = numbers[23:24]
        sublist.sort()
        return sublist[1] if len(sublist) > 1 else None