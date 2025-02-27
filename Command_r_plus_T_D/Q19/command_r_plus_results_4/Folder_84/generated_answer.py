def all_ints_not_div_by_num(lst: list[int]) -> list[int]:
    return [num for num in lst[50:81] if num % 64 != 0]