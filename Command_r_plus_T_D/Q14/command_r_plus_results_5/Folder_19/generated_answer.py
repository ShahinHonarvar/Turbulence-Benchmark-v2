def find_second_smallest_num(numbers: list[int]) -> int:
    sublist = numbers[4:9]
    sublist.sort()
    if len(sublist) < 2:
        return None
    else:
        return sublist[1]