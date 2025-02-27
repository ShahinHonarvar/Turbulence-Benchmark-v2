def all_ints_not_div_by_num(lst: list[int]) -> list[int]:
    return [num for num in lst[2:8] if num % 8 != 0]