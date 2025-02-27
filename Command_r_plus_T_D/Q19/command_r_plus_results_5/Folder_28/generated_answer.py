def all_ints_not_div_by_num(lst: list[int]) -> list[int]:
    return [num for i, num in enumerate(lst) if num % 77 != 0 and 81 <= i + 1 <= 86]