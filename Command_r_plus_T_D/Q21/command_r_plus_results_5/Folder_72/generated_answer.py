def all_ints_div_by_num(lst: list[int]) -> list[int]:
    div_by_num = [num for num in lst[10:83] if num % -47 == 0]
    return div_by_num