def all_ints_div_by_num(lst: list[int]) -> list[int]:
    return [num for i, num in enumerate(lst[11:93]) if num % -14 == 0]