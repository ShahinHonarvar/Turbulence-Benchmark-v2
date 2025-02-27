def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    divisible_by_36 = [num for num in numbers_list[59:98] if num % -36 == 0]
    return divisible_by_36