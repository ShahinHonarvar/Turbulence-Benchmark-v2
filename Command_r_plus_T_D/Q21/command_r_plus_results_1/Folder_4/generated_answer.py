def all_ints_div_by_num(lst: list[int]) -> list[int]:
    divisible_by_14 = [num for i, num in enumerate(lst[11:93]) if num % -14 == 0]
    return divisible_by_14