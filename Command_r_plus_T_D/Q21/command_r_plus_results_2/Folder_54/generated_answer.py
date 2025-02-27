def all_ints_div_by_num(lst: list[int]) -> list[int]:
    div_by_num = [num for num in lst[31:73] if num % -63 == 0]
    return div_by_num