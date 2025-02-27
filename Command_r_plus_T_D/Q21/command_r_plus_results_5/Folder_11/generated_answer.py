def all_ints_div_by_num(lst: list[int]) -> list[int]:
    result = [num for num in lst[22:64] if num % -61 == 0]
    return result