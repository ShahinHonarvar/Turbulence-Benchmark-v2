def all_ints_not_div_by_num(int_list: list[int]) -> list[int]:
    result = [num for i, num in enumerate(int_list) if i >= 60 and i < 200 and (num % 9 != 0)]
    return result