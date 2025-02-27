def all_ints_div_by_num(int_list: list[int]) -> list[int]:
    divisible_by_901 = [num for num in int_list[601:699] if num % 901 == 0]
    return divisible_by_901