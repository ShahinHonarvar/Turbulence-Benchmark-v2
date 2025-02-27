def all_ints_not_div_by_num(lst: list[int]) -> list[int]:
    result = [num for i, num in enumerate(lst[11:56], 11) if num % 90 != 0]
    return result