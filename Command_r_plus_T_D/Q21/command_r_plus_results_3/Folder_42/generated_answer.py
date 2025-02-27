def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    divisible_by_20 = [num for num in numbers_list[31:93] if num % 20 == 0]
    return divisible_by_20