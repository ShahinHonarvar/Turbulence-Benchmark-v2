def all_ints_not_div_by_num(lst: list[int]) -> list[int]:
    return [num for i, num in enumerate(lst[20:50]) if num % 40 != 0]