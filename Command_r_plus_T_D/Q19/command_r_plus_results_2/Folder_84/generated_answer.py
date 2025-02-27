def all_ints_not_div_by_num(int_list: list[int]) -> list[int]:
    result = [num for i, num in enumerate(int_list) if num % 64 != 0 and 50 <= i < 81]
    return result