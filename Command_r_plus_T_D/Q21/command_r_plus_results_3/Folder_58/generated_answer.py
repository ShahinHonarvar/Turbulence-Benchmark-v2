def all_ints_div_by_num(lst: list[int]) -> list[int]:
    result = [num for num in lst[255:619] if num % 965 == 0]
    return result