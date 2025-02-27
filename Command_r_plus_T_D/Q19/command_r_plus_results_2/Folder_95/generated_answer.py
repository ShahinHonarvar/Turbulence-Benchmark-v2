def all_ints_not_div_by_num(lst: list[int]) -> list[int]:
    return [num for i, num in enumerate(lst) if num % -41 != 0 and 38 <= i < 52]