def all_ints_not_div_by_num(lst: list[int]) -> list[int]:
    return [num for i, num in enumerate(lst) if num % -53 != 0 and 25 <= i < 76]